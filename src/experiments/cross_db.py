from datetime import datetime
from querycat.src.experiments.mongodb_native import seed_database_mongodb
from querycat.src.experiments.postgresql_native import seed_database_postgresql
from querycat.src.experiments.settings import EXPERIMENTS_EVOCAT_BASE_URL, EXPERIMENTS_POSTGRESQL_TABLE_NAME
from querycat.src.experiments.setup import setup_mmcat

from querycat.src.quecat import execute_query


def run_experiment_cross_db():
    postgresql_connection = seed_database_postgresql()
    mongodb_collection = seed_database_mongodb()
    schema_id = setup_mmcat(mmcat_base_url=EXPERIMENTS_EVOCAT_BASE_URL)

    db_start_time = datetime.now()
    # Collect all results by converting them to lists
    cursor = postgresql_connection.cursor()
    cursor.execute(
        f"SELECT id, name, surname, address FROM {EXPERIMENTS_POSTGRESQL_TABLE_NAME}"
    )
    postgresql_result = cursor.fetchall()
    mongodb_result = list(
        mongodb_collection.aggregate(
            [{"$project": {"_id": 1, "total_price": 1, "status": 1, "customer_id": 1}}]
        )
    )
    db_end_time = datetime.now()

    quecat_start_time = datetime.now()
    query = """
    SELECT {
        ?order id ?orderId ;
            totalPrice ?totalPrice ;
            status ?status ;
            customerName ?customerName ;
            customerSurname ?customerSurname ;
            address ?customerAddress .
    }
    WHERE {
        ?order 6 ?orderId ;
            7 ?totalPrice ;
            8 ?status ;
            5 ?customer .

        ?customer 2 ?customerName ;
            3 ?customerSurname ;
            4 ?customerAddress .
    }
    """
    result_instance = execute_query(query_string=query, schema_id=schema_id)
    quecat_end_time = datetime.now()

    db_elapsed_ms = (db_end_time - db_start_time).total_seconds() * 1000
    quecat_elapsed_ms = (quecat_end_time - quecat_start_time).total_seconds() * 1000
    print(f"Native databases combined elapsed time: {db_elapsed_ms} ms")
    print(f"MM-quecat elapsed time: {quecat_elapsed_ms} ms")


if __name__ == "__main__":
    run_experiment_cross_db()
