from dataclasses import dataclass
from typing import List
from uuid import uuid4
from querycat.src.parsing.model import Query, Triple, Variable, WhereClause
from querycat.src.querying.instance_model import InstanceCategory
from querycat.src.querying.mapping_model import Mapping
from querycat.src.querying.model import QueryPlan
from querycat.src.querying.schema_model import SchemaCategory
from querycat.src.querying.utils import get_variable_types, is_base_morphism


@dataclass
class QueryEngine:
    schema_category: SchemaCategory
    mappings: List[Mapping]

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
        variable_types = get_variable_types(query, self.schema_category)
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
                triple_kinds_assignments.append((triple, kinds))

        pass

    def select_best_plan(self, plans: List[QueryPlan]) -> QueryPlan:
        ...

    def execute_plan(self, plan: QueryPlan) -> InstanceCategory:
        ...
