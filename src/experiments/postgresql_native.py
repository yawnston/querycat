from datetime import datetime
from querycat.src.experiments.settings import (
    EXPERIMENTS_EVOCAT_BASE_URL,
    EXPERIMENTS_POSTGRESQL_CONNECTION_STRING,
    EXPERIMENTS_POSTGRESQL_NUM_CUSTOMERS,
    EXPERIMENTS_POSTGRESQL_TABLE_NAME,
)
from querycat.src.experiments.setup import setup_mmcat
from faker import Faker
import psycopg2
from querycat.src.quecat import execute_query


def seed_database_postgresql():
    connection = psycopg2.connect(EXPERIMENTS_POSTGRESQL_CONNECTION_STRING)

    # Random data seed for reproducibility
    Faker.seed(42)
    faker = Faker()

    cursor = connection.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {EXPERIMENTS_POSTGRESQL_TABLE_NAME};")
    cursor.execute(
        f"CREATE TABLE {EXPERIMENTS_POSTGRESQL_TABLE_NAME} (id text PRIMARY KEY, name text, surname text, address text);"
    )

    # Generate random seeded data
    for i in range(EXPERIMENTS_POSTGRESQL_NUM_CUSTOMERS):
        cursor.execute(
            f"INSERT INTO {EXPERIMENTS_POSTGRESQL_TABLE_NAME} VALUES (%(id)s, %(name)s, %(surname)s, %(address)s);",
            {
                "id": str(i),
                "name": faker.first_name(),
                "surname": faker.last_name(),
                "address": faker.address(),
            },
        )

    connection.commit()
    cursor.close()

    return connection


def run_experiment_postgresql():
    postgresql_connection = seed_database_postgresql()
    schema_id = setup_mmcat(mmcat_base_url=EXPERIMENTS_EVOCAT_BASE_URL)

    postgresql_start_time = datetime.now()
    cursor = postgresql_connection.cursor()
    cursor.execute(
        f"SELECT id, name, surname, address FROM {EXPERIMENTS_POSTGRESQL_TABLE_NAME}"
    )
    # Collect all results by converting them to a list
    postgresql_result = cursor.fetchall()
    postgresql_end_time = datetime.now()
    assert len(postgresql_result) == EXPERIMENTS_POSTGRESQL_NUM_CUSTOMERS

    quecat_start_time = datetime.now()
    query = """
    SELECT {
        ?customer id ?id ;
            name ?name ;
            surname ?surname ;
            address ?address .
    }
    WHERE {
        ?customer 1 ?id ;
            2 ?name ;
            3 ?surname ;
            4 ?address .
    }
    """
    result_instance = execute_query(query_string=query, schema_id=schema_id)
    quecat_end_time = datetime.now()

    postgresql_elapsed_ms = (
        postgresql_end_time - postgresql_start_time
    ).total_seconds() * 1000
    quecat_elapsed_ms = (quecat_end_time - quecat_start_time).total_seconds() * 1000
    print(f"PostgreSQL elapsed time: {postgresql_elapsed_ms} ms")
    print(f"MM-quecat elapsed time: {quecat_elapsed_ms} ms")


if __name__ == "__main__":
    run_experiment_postgresql()
