from querycat.src.parsing.query_parser import QueryParser
from querycat.src.querying.engine import QueryEngine
from querycat.src.querying.mmcat_client import MMCat

if __name__ == "__main__":
    # query_string = """
    #     SELECT {
    #         ?item name  ?itemName  ;
    #             price ?itemPrice .
    #     }
    #     WHERE {
    #         ?item 13 ?itemName ;
    #             14 ?itemPrice .

    #         FILTER(?itemPrice = "Luxor")
    #     }
    # """
    query_string = """
        SELECT {
            ?order number ?number .
        }
        WHERE {
            ?order 4 ?number .
            FILTER(?number = 2)
        }
    """

    query = QueryParser().parse(query_string)
    mmcat = MMCat(schema_id=1)
    mappings = mmcat.get_mappings()
    schema_category = mmcat.get_schema_category()

    engine = QueryEngine(schema_category=schema_category, mappings=mappings)
    preprocessed_query = engine.preprocess_query(query)
    query_plans = engine.create_plans(preprocessed_query)
    best_plan = engine.select_best_plan(query_plans)
    result_instance = engine.execute_plan(best_plan)
