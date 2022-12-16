from querycat.src.querying.mmcat_client import MMCat
from querycat.src.parsing.query_parser import QueryParser

if __name__ == "__main__":
    query_string = """
        SELECT {
            ?item name  ?itemName  ;
                price ?itemPrice .
        }
        WHERE {
            ?item 56 ?itemName ;
                57 ?itemPrice .

            FILTER(?itemPrice = "Luxor")
        }
    """

    query = QueryParser().parse(query_string)
    mmcat = MMCat(schema_id=1)
    mapping = mmcat.get_mappings()
    schema_category = mmcat.get_schema_category()
    pass
