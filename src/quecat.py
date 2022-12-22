from querycat.src.parsing.query_parser import QueryParser
from querycat.src.projection.projector import QueryProjector
from querycat.src.querying.engine import QueryEngine
from querycat.src.querying.instance_model import InstanceCategory
from querycat.src.querying.mmcat_client import MMCat


def execute_query(query: str, schema_id: int) -> InstanceCategory:
    query = QueryParser().parse(query_string)
    mmcat = MMCat(schema_id=schema_id)
    mappings = mmcat.get_mappings()
    schema_category = mmcat.get_schema_category()

    engine = QueryEngine(
        schema_category=schema_category, mappings=mappings, mmcat=mmcat
    )
    preprocessed_query = engine.preprocess_query(query)
    query_plans = engine.create_plans(preprocessed_query)

    # Create new schema category for WHERE clause and set it as active
    # TODO: do we copy the category earlier? because the mappings are set in variables
    # We have to be careful about using the correct object IDs (they change, object keys don't)
    internal_category_id = 15
    # internal_category_id = mmcat.copy_schema_category()
    mmcat_internal = MMCat(schema_id=internal_category_id)
    engine.mmcat = mmcat_internal

    best_plan = engine.select_best_plan(query_plans)
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
            ?order 9 ?customer ;
                10 ?orderId .
            ?customer 2 ?customerName ;
                3 ?customerSurname .
        }
    """

    result = execute_query(query=query_string, schema_id=4)
    ...
