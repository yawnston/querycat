import json
from typing import List
from querycat.src.open_api_definition_client.api.mapping_controller.get_all_mappings_in_category import (
    sync_detailed as get_all_mappings,
)
from querycat.src.open_api_definition_client.api.schema_category_controller.get_category_wrapper import (
    sync_detailed as get_schema_category,
)
from querycat.src.open_api_definition_client.client import Client
from querycat.src.open_api_definition_client.models.mapping_view import MappingView
from querycat.src.open_api_definition_client.models.schema_category_wrapper import SchemaCategoryWrapper
from querycat.src.querying.mapping_model import Mapping
from querycat.src.querying.schema_model import SchemaCategory


class MMCat:
    def __init__(self, schema_id: int) -> None:
        self.mmcat_client = Client(base_url="http://localhost:27500")
        self.schema_id = schema_id

    def get_mappings(self) -> List[Mapping]:
        response = get_all_mappings(client=self.mmcat_client, schema_id=self.schema_id)
        if response.status_code != 200:
            raise Exception("Response from mmcat was not 200: ", response)
        response_content_json = json.loads(response.content)

        mappings_api = [
            MappingView.from_dict(mapping) for mapping in response_content_json
        ]
        mappings = [Mapping.from_mapping_view(x) for x in mappings_api]
        return mappings

    def get_schema_category(self) -> SchemaCategory:
        response = get_schema_category(client=self.mmcat_client, id=self.schema_id)
        if response.status_code != 200:
            raise Exception("Response from mmcat was not 200: ", response)
        response_content_json = json.loads(response.content)
        category_api = SchemaCategoryWrapper.from_dict(response_content_json)
        schema_category = SchemaCategory.from_category_view(category_api)
        return schema_category
