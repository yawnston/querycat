import json
from time import sleep

from querycat.src.open_api_definition_client.api.job_controller.create_new_job import (
    sync_detailed as create_new_job,
)
from querycat.src.open_api_definition_client.api.job_controller.start_job_with_query import (
    sync_detailed as start_job_with_query,
)
from querycat.src.open_api_definition_client.client import Client
from querycat.src.open_api_definition_client.models.job import Job
from querycat.src.open_api_definition_client.models.new_job_view import NewJobView
from querycat.src.querying.model import QueryPlan


class InstanceMerger:
    def __init__(self):
        self.client = Client(base_url="http://localhost:27500")

    def merge(self, query_plan: QueryPlan):
        new_job_view = NewJobView(
            mapping_id=15,
            type="ModelToCategory",
            name="MyModelToCategory",
        )
        job_response = create_new_job(client=self.client, json_body=new_job_view)
        job_content_json = json.loads(job_response.content)
        job = Job.from_dict(job_content_json)

        query = """SELECT id, name, surname, address_id FROM customer"""
        start_job_response = start_job_with_query(
            client=self.client, id=job.id, json_body=query
        )
        sleep(2)


if __name__ == "__main__":
    merger = InstanceMerger()
    merger.merge(None)
