from querycat.src.parsing.query_parser import QueryParser
from querycat.src.projection.projector import QueryProjector
from querycat.src.querying.engine import QueryEngine
from querycat.src.querying.instance_model import InstanceCategory
from querycat.src.querying.mmcat_client import MMCat
from querycat.src.querying.planner import QueryPlanner
from querycat.src.querying.preprocessor import QueryPreprocessor


def execute_query(
    query_string: str, schema_id: int, mmcat_base_url: str
) -> InstanceCategory:
    """Given a MMQL `query_string`, execute this query against the
    schema category identified by `schema_id` stored in the
    MM-evocat instance hosted at `mmcat_base_url`.

    Returns an instance category with the results of the query.
    """
    query = QueryParser().parse(query_string)
    mmcat = MMCat(schema_id=schema_id, base_url=mmcat_base_url)
    mappings = mmcat.get_mappings()
    schema_category = mmcat.get_schema_category()

    preprocessed_query = QueryPreprocessor().preprocess_query(query)
    planner = QueryPlanner(schema_category=schema_category, mappings=mappings)
    query_plans = planner.create_plans(preprocessed_query)

    internal_category_id = mmcat.copy_schema_category()
    mmcat_internal = MMCat(schema_id=internal_category_id, base_url=mmcat_base_url)
    engine = QueryEngine(schema_category=schema_category, mmcat=mmcat_internal)

    best_plan = planner.select_best_plan(query_plans)
    engine.compile_statements(best_plan)
    where_instance = engine.execute_plan(best_plan)

    projector = QueryProjector()
    result_schema, result_instance = projector.project(
        plan=best_plan, where_instance=where_instance
    )
    return result_instance


if __name__ == "__main__":
    query_string = """
        SELECT {
            ?order orderId ?orderId ; 
                customerName ?customerName ;
                customerSurname ?customerSurname .
        }
        WHERE {
            ?customer -9 ?order ;
                2 ?customerName ;
                3 ?customerSurname .

            ?order 10 ?orderId .

            FILTER(?customerName = "Alice")
        }
    """

    result = execute_query(
        query_string=query_string, schema_id=4, mmcat_base_url="http://localhost:27500"
    )
    ...
