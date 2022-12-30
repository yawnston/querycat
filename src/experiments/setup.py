from dataclasses import dataclass
import json
from querycat.src.experiments.settings import (
    EXPERIMENTS_MONGODB_MAPPING_JSON,
    EXPERIMENTS_MONGODB_ROOT_OBJECT_KEY,
    EXPERIMENTS_POSTGRESQL_MAPPING_JSON,
    EXPERIMENTS_POSTGRESQL_ROOT_OBJECT_KEY,
    EXPERIMENTS_SCHEMA_CATEGORY_JSON,
)
from querycat.src.open_api_definition_client.models.mapping_init import MappingInit
from querycat.src.querying.mmcat_client import MMCat


def setup_mmcat(mmcat_base_url: str) -> int:
    """Set up the experiments schema and mapping in MM-cat.

    Returns the id of the created schema category."""
    mmcat = MMCat(schema_id=None, base_url=mmcat_base_url)
    schema_id = mmcat.create_schema_category()
    mmcat.schema_id = schema_id
    mmcat.put_schema_category_content(schema_id, EXPERIMENTS_SCHEMA_CATEGORY_JSON)

    mongodb_mapping_dict = json.loads(EXPERIMENTS_MONGODB_MAPPING_JSON)
    mongodb_mapping_init = MappingInit.from_dict(mongodb_mapping_dict)
    mongodb_mapping_init.category_id = schema_id
    mongodb_mapping_init.root_object_id = (
        mmcat.get_schema_category()
        .get_object_by_key(key=EXPERIMENTS_MONGODB_ROOT_OBJECT_KEY)
        .id
    )
    mmcat.create_mapping(mongodb_mapping_init)

    postgresql_mapping_dict = json.loads(EXPERIMENTS_POSTGRESQL_MAPPING_JSON)
    postgresql_mapping_init = MappingInit.from_dict(postgresql_mapping_dict)
    postgresql_mapping_init.category_id = schema_id
    postgresql_mapping_init.root_object_id = (
        mmcat.get_schema_category()
        .get_object_by_key(key=EXPERIMENTS_POSTGRESQL_ROOT_OBJECT_KEY)
        .id
    )
    mmcat.create_mapping(postgresql_mapping_init)

    return schema_id
