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
    # query_string = """
    #     SELECT {
    #         ?order id ?orderId ;
    #             customerName ?customerName .
    #     }
    #     WHERE {
    #         ?order 10 ?orderId ;
    #             9/2 ?customerName .
    #     }
    # """
    query_string = """
        SELECT {
            ?order orderId ?orderId ; 
                customerName ?customerName ;
                customerSurname ?customerSurname .
        }
        WHERE {
            ?order 9 ?customer ;
                10 ?orderId .
            ?customer 2 ?customerName .
        }
    """

    query = QueryParser().parse(query_string)
    mmcat = MMCat(schema_id=4)
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
    instance = engine.execute_plan(best_plan)

    morphism2 = mmcat_internal.get_instance_morphism(signature=2)
    morphism9 = mmcat_internal.get_instance_morphism(signature=9)
    morphism10 = mmcat_internal.get_instance_morphism(signature=10)
    ...
