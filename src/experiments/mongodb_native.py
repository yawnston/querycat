from datetime import datetime
from querycat.src.experiments.settings import (
    EXPERIMENTS_EVOCAT_BASE_URL,
    EXPERIMENTS_MONGODB_COLLECTION_NAME,
    EXPERIMENTS_MONGODB_CONNECTION_STRING,
    EXPERIMENTS_MONGODB_NUM_ORDERS,
    EXPERIMENTS_POSTGRESQL_NUM_CUSTOMERS,
)
from querycat.src.experiments.setup import setup_mmcat
from pymongo import MongoClient
from faker import Faker

from querycat.src.quecat import execute_query


def seed_database_mongodb():
    mongo_client = MongoClient(EXPERIMENTS_MONGODB_CONNECTION_STRING)
    database = mongo_client.get_database()
    # Clean out data from previous experiment runs
    database.drop_collection(name_or_collection=EXPERIMENTS_MONGODB_COLLECTION_NAME)
    collection = database.get_collection(name=EXPERIMENTS_MONGODB_COLLECTION_NAME)

    # Random data seed for reproducibility
    Faker.seed(42)
    faker = Faker()

    # Generate random seeded data
    orders = []
    for i in range(EXPERIMENTS_MONGODB_NUM_ORDERS):
        orders.append(
            {
                "_id": str(i),
                # Make sure that customer ids correlate to PostgreSQL customer ids
                "customer_id": str(i % EXPERIMENTS_POSTGRESQL_NUM_CUSTOMERS),
                "total_price": faker.random_int(min=1, max=9999),
                "status": faker.random_element(
                    elements=(
                        "Awaiting Payment",
                        "Awaiting Transit",
                        "In Transit",
                        "Completed",
                    )
                ),
            }
        )

    insert_result = collection.insert_many(orders)
    assert len(insert_result.inserted_ids) == EXPERIMENTS_MONGODB_NUM_ORDERS

    return collection


def run_experiment_mongodb():
    collection = seed_database_mongodb()
    schema_id = setup_mmcat(mmcat_base_url=EXPERIMENTS_EVOCAT_BASE_URL)

    mongodb_start_time = datetime.now()
    # Collect all results by converting them to a list
    mongodb_result = list(
        collection.aggregate(
            [{"$project": {"_id": 1, "total_price": 1, "status": 1, "customer_id": 1}}]
        )
    )
    mongodb_end_time = datetime.now()

    quecat_start_time = datetime.now()
    # Can we optimize the ?customerId by inlining it in the schema category?
    # That would eliminate the need for instance morphism contraction.
    query = """
    SELECT {
        ?order id ?orderId ;
            totalPrice ?totalPrice ;
            status ?status ;
            customerId ?customerId .
    }
    WHERE {
        ?order 6 ?orderId ;
            7 ?totalPrice ;
            8 ?status ;
            5/1 ?customerId .
    }
    """
    result_instance, _ = execute_query(
        query_string=query,
        schema_id=schema_id,
        mmcat_base_url=EXPERIMENTS_EVOCAT_BASE_URL,
    )
    quecat_end_time = datetime.now()

    mongodb_elapsed_ms = (mongodb_end_time - mongodb_start_time).total_seconds() * 1000
    quecat_elapsed_ms = (quecat_end_time - quecat_start_time).total_seconds() * 1000
    print(f"MongoDB elapsed time: {mongodb_elapsed_ms} ms")
    print(f"MM-quecat elapsed time: {quecat_elapsed_ms} ms")


if __name__ == "__main__":
    run_experiment_mongodb()
