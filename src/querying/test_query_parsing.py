from querycat.src.querying.query_parser import QueryParser

if __name__ == "__main__":
    query_string = """
        SELECT {
            ?item name  ?itemName  ;
                price ?itemPrice .
        }
        WHERE {
            ?item 56 ?itemName ;
                57 ?itemPrice .
        }
    """
    QueryParser().parse(query_string)
