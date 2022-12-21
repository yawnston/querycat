import json
from time import sleep
from querycat.src.open_api_definition_client.api.instance_category_controller.get_instance_object_1 import (
    sync_detailed as get_instance_object,
)
from querycat.src.open_api_definition_client.api.instance_category_controller.get_instance_morphism import (
    sync_detailed as get_instance_morphism,
)

from querycat.src.open_api_definition_client.api.job_controller.create_new_job import (
    sync_detailed as create_new_job,
)
from querycat.src.open_api_definition_client.api.job_controller.start_job_with_query import (
    sync_detailed as start_job_with_query,
)
from querycat.src.open_api_definition_client.client import Client
from querycat.src.open_api_definition_client.models.instance_morphism_view import (
    InstanceMorphismView,
)
from querycat.src.open_api_definition_client.models.instance_object_view import (
    InstanceObjectView,
)
from querycat.src.open_api_definition_client.models.job import Job
from querycat.src.open_api_definition_client.models.new_job_view import NewJobView
from querycat.src.querying.model import QueryPlan

import httpx

class InstanceMerger:
    def __init__(self, schema_id: int):
        self.client = Client(base_url="http://localhost:27500")
        self.schema_id = schema_id
        # Instance category manipulation doesn't work without using cookies
        cookies_response = httpx.get(f"{self.client.base_url}/instances")
        self.client.cookies = cookies_response.cookies

    def run_job(self, query: str, mapping_id: int, object_key: int, signature: int):
        new_job_view = NewJobView(
            mapping_id=mapping_id,
            type="ModelToCategory",
            name="MyModelToCategory",
        )
        job_response = create_new_job(client=self.client, json_body=new_job_view)
        job_content_json = json.loads(job_response.content)
        job = Job.from_dict(job_content_json)

        start_job_response = start_job_with_query(
            client=self.client, id=job.id, json_body=query
        )

        object_response = get_instance_object(
            client=self.client, schema_id=self.schema_id, object_key=object_key
        )
        object_response_json = json.loads(object_response.content)
        object = InstanceObjectView.from_dict(object_response_json)

        morphism_response = get_instance_morphism(
            client=self.client, schema_id=self.schema_id, signature=signature
        )
        morphism_response_json = json.loads(morphism_response.content)
        morphism = InstanceMorphismView.from_dict(morphism_response_json)
        pass

    def merge(self, query_plan: QueryPlan):
        pg_query = """SELECT id, name, surname, address_id FROM customer"""
        mongo_query = """db.order.aggregate( [ { $project : { "_id": 1, "customer_id": 1, "items": 1 } } ] )"""
        self.run_job(pg_query, 15, 1, 2)
        self.run_job(mongo_query, 17, 10, 11)


if __name__ == "__main__":
    merger = InstanceMerger(schema_id=4)
    merger.merge(None)
