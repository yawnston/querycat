from dataclasses import dataclass
import itertools
from typing import List
from uuid import uuid4
from querycat.src.parsing.model import Query, Triple, Variable
from querycat.src.querying.mapping_model import Mapping
from querycat.src.querying.mmcat_client import MMCat
from querycat.src.querying.model import (
    InvalidQueryPlanError,
    Kind,
    QueryPart,
    QueryPlan,
    VariableTypes,
)

from querycat.src.querying.schema_model import SchemaCategory
from querycat.src.querying.utils import get_variable_types_from_query


@dataclass
class QueryPlanner:
    schema_category: SchemaCategory
    mappings: List[Mapping]

    def create_plans(self, query: Query) -> List[QueryPlan]:
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
            statements=[],
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
                        statements=[],
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
        raise InvalidQueryPlanError("Missing join point")

    def select_best_plan(self, plans: List[QueryPlan]) -> QueryPlan:
        # Selection of the best plan is outside the scope of my thesis,
        # but I will probably soon add some basic algorithm for this.
        return plans[0]
