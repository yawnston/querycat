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
    """Query planner class which is responsible for the creation of query
    plans for a given query"""

    schema_category: SchemaCategory
    mappings: List[Mapping]

    def create_plans(self, query: Query) -> List[QueryPlan]:
        """Given an input query, generate all possible query plans.
        In the case of no data redundancy, the result will always
        contain only one query plan. In the case that redundancy is
        present, there can be multiple plans.
        """
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
                query_plan = self._create_plan_from_assignment(
                    query, variable_types, assignment
                )
                query_plans.append(query_plan)
            except InvalidQueryPlanError:
                continue

        return query_plans

    def _create_plan_from_assignment(
        self, query: Query, variable_types: VariableTypes, assignment: tuple
    ) -> QueryPlan:
        initial_query_part = QueryPart(
            triples_mapping=[
                (triple, Kind(mapping=mapping)) for triple, mapping in assignment
            ],
            statements=[],
        )
        finished_query_parts: List[QueryPart] = []
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

            split_query_parts = self._split_single_query_part(
                variable_types, query_part
            )
            query_part_queue.extend(split_query_parts)

        self._assign_statements_to_parts(query=query, parts=finished_query_parts)

        return QueryPlan(
            query=query, deferred_statements=[], parts=finished_query_parts, cost=0,
        )

    def _split_single_query_part(
        self, variable_types: VariableTypes, query_part: QueryPart
    ) -> List[QueryPart]:
        # Match triples pattern () -A-> (I) -B-> () or () <-A- (I) -B-> ()
        for tripleA, kindA in query_part.triples_mapping:
            for tripleB, kindB in query_part.triples_mapping:
                if (
                    tripleA.object == tripleB.subject
                    or tripleA.subject == tripleB.subject
                ):
                    # This condition needs to change in the cases of databases without joins,
                    # but MM-evocat doesn't support joins yet anyway.
                    if kindA.mapping.database.id == kindB.mapping.database.id:
                        continue

                    return self._split_join_point(
                        variable_types, query_part, tripleA, kindA, tripleB, kindB
                    )
        raise InvalidQueryPlanError("Missing join point")

    def _split_join_point(
        self,
        variable_types: VariableTypes,
        query_part: QueryPart,
        tripleA: Triple,
        kindA: Kind,
        tripleB: Triple,
        kindB: Kind,
    ) -> List[QueryPart]:
        intersection_var = tripleB.subject
        intersection_object = variable_types[intersection_var.name]
        intersection_identifier = None
        for identifier in intersection_object.ids:
            if all(
                (
                    all(
                        (
                            kindA.mapping.get_property_name(str(base_morphism))
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

        # When MM-evocat supports joins and we can implement them,
        # non-contiguous database parts (like mongo-postgre-mongo) could
        # leave gaps in the query parts with this implementation.
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
                # In the case that an identifier is a compound signature,
                # this will not suffice.
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
                                # Note that the variable name will be different for both
                                # query parts, but this is not a problem since the morphisms
                                # dictate data placement when joining instance categories.
                                object=Variable(name=uuid4().hex),
                            ),
                            select_kind,
                        )
                    )

        return [new_query_part, query_part]

    def _assign_statements_to_parts(self, query: Query, parts: List[QueryPart]) -> None:
        """Given a list of finished query parts for a query plan, go through the non-triple
        statements in the query and assign them to query parts.

        Note that a single statement may be assigned to multiple query parts, for example
        filtering the value of a variable which is selected from multiple query parts
        must naturally apply this filter to all relevant query parts.
        """
        for part in parts:
            for filter in query.where.filters:
                for triple, _ in part.triples_mapping:
                    if isinstance(filter.lhs, Variable) and filter.lhs == triple.object:
                        # Whenever we implement deferred statements, we will need to
                        # check whether a potential rhs variable/aggregation is in the same
                        # query part.
                        part.statements.append(filter)

            for values in query.where.values:
                for triple, _ in part.triples_mapping:
                    if values.variable == triple.object:
                        part.statements.append(values)

    def select_best_plan(self, plans: List[QueryPlan]) -> QueryPlan:
        """Given a set of query plans, evaluate the cost of each plan
        and return the best plan.
        """
        # Selection of the best plan is outside the scope of my thesis,
        # but I will probably soon add some basic algorithm for this.
        return plans[0]
