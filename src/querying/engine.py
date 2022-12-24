from dataclasses import dataclass
import itertools
from typing import List
from uuid import uuid4
from querycat.src.merging.instance_merger import InstanceMerger
from querycat.src.open_api_definition_client.models.mapping_init import MappingInit

from querycat.src.parsing.model import Query, Triple, Variable, WhereClause
from querycat.src.querying.instance_model import InstanceCategory
from querycat.src.querying.mapping_model import Mapping, Signature
from querycat.src.querying.mmcat_client import MMCat
from querycat.src.querying.model import (
    InvalidQueryPlanError,
    Kind,
    QueryPart,
    QueryPartCompiled,
    QueryPlan,
    VariableTypes,
)
from querycat.src.querying.schema_model import SchemaCategory
from querycat.src.querying.utils import (
    get_variable_types_from_part,
    get_variable_types_from_query,
    is_base_morphism,
    is_object_terminal,
)
from querycat.src.wrappers.wrapper import Wrapper


@dataclass
class QueryEngine:
    schema_category: SchemaCategory
    mappings: List[Mapping]
    mmcat: MMCat

    def preprocess_query(self, query: Query) -> Query:
        where = WhereClause(
            filters=query.where.filters,
            variables=query.where.variables,
            triples=self._simplify_triples(query.where.triples),
        )
        return Query(
            variables=query.variables,
            select=query.select,
            where=where,
        )

    def _simplify_triples(self, triples: List[Triple]) -> List[Triple]:
        transformed_triples = []

        for triple in triples:
            if is_base_morphism(triple.morphism):
                transformed_triples.append(triple)
            else:
                split_morphisms = triple.morphism.split("/")
                split_triples = [
                    Triple(
                        subject=None,
                        morphism=x,
                        object=None,
                    )
                    for x in split_morphisms
                ]

                split_triples[0].subject = triple.subject
                split_triples[-1].object = triple.object

                for i in range(0, len(split_triples) - 1):
                    new_variable = Variable(name=uuid4().hex)
                    split_triples[i].object = new_variable
                    split_triples[i + 1].subject = new_variable

                transformed_triples.extend(split_triples)

        return transformed_triples

    def create_plans(self, query: Query) -> List[QueryPlan]:
        #   For each pair of triples (cartesian product of the two plans):
        #       If pair of triples matches pattern () -A-> (I) -B-> () or () <-A- (I) -B-> ():
        #           For each identifier in ids(I):
        #               If identifier is in kind(A) and kind(B):
        #                   can_join = True
        #                   Add identifier projection to both A and B query parts
        #           If not can_join:
        #               Eliminate this query plan

        variable_types = get_variable_types_from_query(
            query=query, schema_category=self.schema_category
        )
        used_schema_object_ids = {x.id for x in variable_types.values()}
        triple_kinds_assignments = []
        for triple in query.where.triples:
            kinds = [x for x in self.mappings if x.get_property_name(triple.morphism)]
            kinds = [x for x in kinds if x.root_object_id in used_schema_object_ids]
            if len(kinds) == 0:
                raise Exception(
                    "Cannot create query plan - morphism not in mapping or root object not in mapping"
                )
            else:
                triple_kinds_assignments.append([(triple, kind) for kind in kinds])

        assignments_product = list(itertools.product(*triple_kinds_assignments))

        query_plans = []
        for assignment in assignments_product:
            try:
                query_plan = self.split_query_parts(query, variable_types, assignment)
                query_plans.append(query_plan)
            except InvalidQueryPlanError:
                continue

        # FIXME: this generates different variable names for the same join point in two query parts,
        # is that a problem? and how about when one side already has it but one doesn't? do we take over
        # the same variable name?
        return query_plans

    def split_query_parts(
        self, query: Query, variable_types: VariableTypes, assignment: tuple
    ) -> QueryPlan:
        initial_query_part = QueryPart(
            triples_mapping=[
                (triple, Kind(mapping=mapping)) for triple, mapping in assignment
            ],
        )
        finished_query_parts = []
        query_part_queue = [initial_query_part]
        while query_part_queue:
            query_part = query_part_queue.pop()
            if (
                len(
                    {kind.mapping.database.id for _, kind in query_part.triples_mapping}
                )
                == 1
            ):
                finished_query_parts.append(query_part)
                continue

            split_query_parts = self.split_single_query_part(variable_types, query_part)
            query_part_queue.extend(split_query_parts)

        return QueryPlan(
            query=query, deferred_statements=[], parts=finished_query_parts
        )

    def split_single_query_part(self, variable_types, query_part) -> List[QueryPart]:
        # Match triples pattern () -A-> (I) -B-> () or () <-A- (I) -B-> ()
        for tripleA, kindA in query_part.triples_mapping:
            for tripleB, kindB in query_part.triples_mapping:
                if (
                    tripleA.object == tripleB.subject
                    or tripleA.subject == tripleB.subject
                ):
                    # TODO: databases without joins would need this changed
                    if kindA.mapping.database.id == kindB.mapping.database.id:
                        continue

                    intersection_var = tripleB.subject
                    intersection_object = variable_types[intersection_var.name]
                    intersection_identifier = None
                    for identifier in intersection_object.ids:
                        if all(
                            (
                                all(
                                    (
                                        kindA.mapping.get_property_name(
                                            str(base_morphism)
                                        )
                                        for base_morphism in signature.ids
                                    )
                                )
                                for signature in identifier.signatures
                            )
                        ):
                            intersection_identifier = identifier

                            # Project identifier from both kinds and split query part
                    if not intersection_identifier:
                        raise InvalidQueryPlanError(tripleA, tripleB)

                        # TODO: non-contiguous database parts (like mongo-postgre-mongo), with this they leave gaps in the query parts
                    new_query_part = QueryPart(
                        triples_mapping=[
                            (triple, kind)
                            for triple, kind in query_part.triples_mapping
                            if kind.mapping.database.id == kindB.mapping.database.id
                        ],
                    )
                    query_part.triples_mapping = [
                        x
                        for x in query_part.triples_mapping
                        if x not in new_query_part.triples_mapping
                    ]

                    for query_part_to_modify, select_kind in [
                        (new_query_part, kindB),
                        (query_part, kindA),
                    ]:
                        for signature in intersection_identifier.signatures:
                            # TODO: compound signatures in identifiers
                            morphism = signature.ids[0]
                            if not any(
                                (
                                    triple
                                    for triple, _ in query_part_to_modify.triples_mapping
                                    if triple.subject.name == intersection_var.name
                                    and triple.morphism == str(morphism)
                                )
                            ):
                                query_part_to_modify.triples_mapping.append(
                                    (
                                        Triple(
                                            subject=intersection_var,
                                            morphism=str(morphism),
                                            object=Variable(name=uuid4().hex),
                                        ),
                                        select_kind,
                                    )
                                )

                    return [new_query_part, query_part]
        raise InvalidQueryPlanError("Missing join point?")

    def select_best_plan(self, plans: List[QueryPlan]) -> QueryPlan:
        # TODO: implement selection of the best plan (out of scope of my thesis)
        return plans[0]

    def compile_statements(self, plan: QueryPlan) -> None:
        new_schema_category = self.mmcat.get_schema_category()
        for part in plan.parts:
            variable_types = get_variable_types_from_part(part, self.schema_category)
            wrapper = Wrapper.create(mapping=part.triples_mapping[0][1].mapping)

            for statement, kind in part.triples_mapping:
                # TODO: statement can also be other things than just a triple
                if isinstance(statement, Triple):
                    subject = statement.subject
                    morphism = statement.morphism
                    object = statement.object

                    if isinstance(object, str):
                        raise Exception(
                            "Triples with string objects not yet implemented."
                        )
                    elif isinstance(object, Variable):
                        # TODO: nested properties in Mongo
                        if is_object_terminal(variable_types[object.name]):
                            wrapper.add_projection(
                                kind_name=kind.mapping.kind_name,
                                property_name=kind.mapping.get_property_name(morphism),
                                signature=kind.mapping.get_signature(morphism),
                            )
                else:
                    raise Exception("Unknown statement type.")

            # TODO: determining root object id in case of joins, this works only for no joins
            root_kind_mapping = part.triples_mapping[0][1].mapping
            root_object_key = self.schema_category.get_object(
                root_kind_mapping.root_object_id
            ).key
            new_root_object = new_schema_category.get_object_by_key(
                key=root_object_key.value
            )
            mapping_init = MappingInit(
                category_id=self.mmcat.schema_id,
                json_value='{"name": "queryPartKind"}',
                mapping_json_value=Mapping(
                    pkey=root_kind_mapping.pkey,
                    access_path=wrapper.build_access_path(),
                    kind_name=root_kind_mapping.kind_name,
                    database=root_kind_mapping.database,
                    root_object_id=new_root_object.id,
                    root_morphism_id=None,
                    category_id=self.mmcat.schema_id,
                ).to_mapping_json_value(),
                root_object_id=new_root_object.id,
                database_id=root_kind_mapping.database.id,
            )
            part.compiled = QueryPartCompiled(
                db_query=wrapper.build_statement(),
                mapping_init=mapping_init,
            )

    def execute_plan(self, plan: QueryPlan) -> InstanceCategory:
        merger = InstanceMerger(mmcat=self.mmcat)
        return merger.merge(query_plan=plan)
