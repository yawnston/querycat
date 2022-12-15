import json
from typing import List
from querycat.src.open_api_definition_client.api.mapping_controller.get_all_mappings_in_category import (
    sync_detailed as get_all_mappings,
)
from querycat.src.open_api_definition_client.client import Client
from querycat.src.open_api_definition_client.models.mapping_view import MappingView
from querycat.src.querying.mapping_model import Mapping
from querycat.src.parsing.model import Query


class Mapper:
    def get_mappings(self, query: Query) -> List[Mapping]:
        mmcat_client = Client(base_url="http://localhost:27500")
        response = get_all_mappings(client=mmcat_client, schema_id=1)
        if response.status_code != 200:
            raise Exception("Response from mmcat was not 200: ", response)
        response_content_json = json.loads(response.content)
        mappings_api = [MappingView.from_dict(mapping) for mapping in response_content_json]
        mappings = [Mapping.from_mapping_view(x) for x in mappings_api]
        return mappings
