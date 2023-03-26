from dataclasses import dataclass
from typing import List, Tuple
from querycat.src.parsing.model import Query, SelectClause, Variable, WhereClause
from querycat.src.parsing.query_parser import QueryParser
from querycat.src.querying.engine import QueryEngine
from querycat.src.querying.mmcat_client import MMCat

from querycat.src.querying.model import QueryPlan
from querycat.src.querying.planner import QueryPlanner
from querycat.src.querying.preprocessor import QueryPreprocessor
from querycat.src.querying.utils import get_variable_types_from_query


@dataclass
class SchemaObjectInfo:
    key: int
    is_in_projection: bool
    is_in_query: bool
    is_in_filter: bool
    is_in_aggregation: bool
    database_ids: List[str]


def create_query_plans(
    query_string: str, schema_id: int, mmcat_base_url: str, get_db_info: bool
) -> Tuple[List[QueryPlan], List[List[SchemaObjectInfo]]]:
    try:
        query = QueryParser().parse(query_string)
    except:
        query = Query(
            select=SelectClause([], []), variables=[], where=WhereClause([], [], [], [])
        )
    mmcat = MMCat(schema_id=schema_id, base_url=mmcat_base_url)
    mappings = mmcat.get_mappings()
    schema_category = mmcat.get_schema_category()

    preprocessed_query = QueryPreprocessor().preprocess_query(query)
    planner = QueryPlanner(schema_category=schema_category, mappings=mappings)
    query_plans = planner.create_plans(preprocessed_query)

    if get_db_info:
        internal_category_id = mmcat.copy_schema_category()
        mmcat_internal = MMCat(schema_id=internal_category_id, base_url=mmcat_base_url)
        engine = QueryEngine(schema_category=schema_category, mmcat=mmcat_internal)

        # TODO: compile for all plans?
        new_plans = []
        for plan in query_plans:
            try:
                engine.compile_statements(plan)
                new_plans.append(plan)
            except:
                pass
        query_plans = new_plans

    object_infos = []
    variable_types = get_variable_types_from_query(preprocessed_query, schema_category)
    for plan in query_plans:
        object_info = []
        for schema_obj in schema_category.objects:
            databases = []
            object_var = next(
                iter([var for var, obj in variable_types.items() if obj == schema_obj]),
                None,
            )
            if not object_var:
                object_info.append(
                    SchemaObjectInfo(
                        key=schema_obj.key.value,
                        database_ids=[],
                        is_in_aggregation=False,
                        is_in_filter=False,
                        is_in_projection=False,
                        is_in_query=False,
                    )
                )
                continue

            if get_db_info:
                for part in plan.parts:
                    matching_kinds = [
                        kind
                        for triple, kind in part.triples_mapping
                        if (
                            triple.subject.name == object_var
                            or (
                                not isinstance(triple.object, str)
                                and triple.object.name == object_var
                            )
                        )
                    ]
                    for kind in matching_kinds:
                        databases.append(kind.mapping.database.id)

            object_info.append(
                SchemaObjectInfo(
                    key=schema_obj.key.value,
                    database_ids=list(set(databases)),
                    is_in_aggregation=False,
                    is_in_filter=any(
                        [
                            x
                            for x in preprocessed_query.where.filters
                            if (
                                isinstance(x.lhs, Variable) and x.lhs.name == object_var
                            )
                            or (
                                isinstance(x.rhs, Variable) and x.rhs.name == object_var
                            )
                        ]
                        + [
                            x
                            for x in preprocessed_query.where.values
                            if x.variable.name == object_var
                        ]
                    ),
                    is_in_projection=any(
                        [
                            x
                            for x in preprocessed_query.select.triples
                            if (
                                x.subject.name == object_var
                                or (
                                    isinstance(x.object, Variable)
                                    and x.object.name == object_var
                                )
                            )
                        ]
                    ),
                    is_in_query=any(
                        [
                            x
                            for x in preprocessed_query.where.triples
                            if (
                                x.subject.name == object_var
                                or (
                                    isinstance(x.object, Variable)
                                    and x.object.name == object_var
                                )
                            )
                        ]
                    ),
                )
            )

        object_infos.append(object_info)

    return query_plans, object_infos
