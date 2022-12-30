import json
from typing import List
from querycat.src.open_api_definition_client.api.mapping_controller.create_new_mapping import (
    sync_detailed as create_new_mapping,
)

from querycat.src.open_api_definition_client.api.mapping_controller.get_all_mappings_in_category import (
    sync_detailed as get_all_mappings,
)
from querycat.src.open_api_definition_client.api.schema_category_controller.create_new_schema import (
    sync_detailed as create_new_schema,
)
from querycat.src.open_api_definition_client.api.schema_category_controller.get_category_wrapper import (
    sync_detailed as get_schema_category,
)
from querycat.src.open_api_definition_client.api.schema_category_controller.update_category_wrapper import (
    sync_detailed as update_category_wrapper,
)
from querycat.src.open_api_definition_client.client import Client
from querycat.src.open_api_definition_client.models.mapping_init import MappingInit
from querycat.src.open_api_definition_client.models.mapping_view import MappingView
from querycat.src.open_api_definition_client.models.new_job_view import NewJobView
from querycat.src.open_api_definition_client.models.position import Position
from querycat.src.open_api_definition_client.models.schema_category_init import (
    SchemaCategoryInit,
)
from querycat.src.open_api_definition_client.models.schema_category_update import (
    SchemaCategoryUpdate,
)
from querycat.src.open_api_definition_client.models.schema_category_wrapper import (
    SchemaCategoryWrapper,
)
from querycat.src.open_api_definition_client.models.schema_morphism_update import (
    SchemaMorphismUpdate,
)
from querycat.src.open_api_definition_client.models.schema_object_update import (
    SchemaObjectUpdate,
)
from querycat.src.querying.mapping_model import Mapping
from querycat.src.querying.schema_model import SchemaCategory

import json
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
import httpx


class MMCat:
    """Client for MM-evocat (and other MM-cat related services in the future).
    Configure this class with the ID of the schema category you wish to operate on,
    as well as the base URL of the MM-evocat instance.

    All methods of this class correspond to API calls on MM-evocat.
    This class internally uses client code which was automatically generated
    from the OpenAPI specification for MM-evocat which I generated.
    You can re-generate the client yourself using `make openapi-generate`
    from the Makefile provided in this repository.
    """

    def __init__(self, schema_id: int, base_url: str) -> None:
        self.client = Client(base_url=base_url)
        self.schema_id = schema_id

        # Instance category manipulation doesn't work without using cookies
        cookies_response = httpx.get(f"{self.client.base_url}/instances")
        self.client.cookies = cookies_response.cookies

    def get_mappings(self) -> List[Mapping]:
        response = get_all_mappings(client=self.client, schema_id=self.schema_id)
        if response.status_code != 200:
            raise Exception("Response from mmcat was not 200: ", response)
        response_content_json = json.loads(response.content)

        mappings_api = [
            MappingView.from_dict(mapping) for mapping in response_content_json
        ]
        mappings = [Mapping.from_mapping_view(x) for x in mappings_api]
        return mappings

    def get_schema_category(self) -> SchemaCategory:
        response = get_schema_category(client=self.client, id=self.schema_id)
        if response.status_code != 200:
            raise Exception("Response from mmcat was not 200: ", response)
        response_content_json = json.loads(response.content)
        category_api = SchemaCategoryWrapper.from_dict(response_content_json)
        schema_category = SchemaCategory.from_category_view(category_api)
        return schema_category

    def create_schema_category(self) -> int:
        new_schema_response = create_new_schema(
            client=self.client,
            json_body=SchemaCategoryInit(
                json_value='{"name": "MM-quecat schema category"}',
            ),
        )
        new_schema_response_dict = json.loads(new_schema_response.content)
        new_schema_id = new_schema_response_dict["id"]
        return new_schema_id

    def put_schema_category_content(self, id: int, json_body_str: str):
        class TempCategoryContent:
            def __init__(self, json_body_dict):
                self.json_body_dict = json_body_dict

            def to_dict(self):
                return self.json_body_dict

        json_body_dict = json.loads(json_body_str)
        # Workaround to use the deserialized object
        json_body = TempCategoryContent(json_body_dict)
        put_response = update_category_wrapper(
            client=self.client,
            id=id,
            json_body=json_body,
        )

        if put_response.status_code != 200:
            raise Exception("Response from mmcat was not 200: ", put_response)

    def copy_schema_category(self) -> int:
        schema_response = get_schema_category(client=self.client, id=self.schema_id)
        schema_response_dict = json.loads(schema_response.content)
        new_schema_id = self.create_schema_category()

        update_response = update_category_wrapper(
            client=self.client,
            id=new_schema_id,
            json_body=SchemaCategoryUpdate(
                objects=[
                    SchemaObjectUpdate(
                        temporary_id=obj["id"],
                        json_value=obj["jsonValue"],
                        position=Position(
                            x=obj["position"]["x"], y=obj["position"]["y"]
                        ),
                    )
                    for obj in schema_response_dict["objects"]
                ],
                morphisms=[
                    SchemaMorphismUpdate(
                        temporary_cod_id=morphism["codId"],
                        temporary_dom_id=morphism["domId"],
                        json_value=morphism["jsonValue"],
                    )
                    for morphism in schema_response_dict["morphisms"]
                ],
            ),
        )
        if update_response.status_code != 200:
            raise Exception("Response from mmcat was not 200: ", update_response)

        return new_schema_id

    def run_job_with_query(
        self,
        query: str,
        mapping_id: int,
    ):
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
        if start_job_response.status_code != 200:
            raise Exception("Starting job failed: ", start_job_response)

    def get_instance_object(self, object_key: int) -> InstanceObjectView:
        object_response = get_instance_object(
            client=self.client, schema_id=self.schema_id, object_key=object_key
        )
        object_response_json = json.loads(object_response.content)
        object = InstanceObjectView.from_dict(object_response_json)
        return object

    def get_instance_morphism(self, signature: int) -> InstanceMorphismView:
        morphism_response = get_instance_morphism(
            client=self.client, schema_id=self.schema_id, signature=signature
        )
        morphism_response_json = json.loads(morphism_response.content)
        morphism = InstanceMorphismView.from_dict(morphism_response_json)
        return morphism

    def create_mapping(self, mapping: MappingInit) -> int:
        response = create_new_mapping(client=self.client, json_body=mapping)
        if response.status_code != 200:
            raise Exception("Mapping creation failed: ", response)
        response_json = json.loads(response.content)
        mapping_view = MappingView.from_dict(response_json)
        return mapping_view.id
