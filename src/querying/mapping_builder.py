from typing import Dict, List, Tuple
from querycat.src.open_api_definition_client.models.mapping_init import MappingInit
from querycat.src.querying.mapping_model import (
    AccessPath,
    ComplexProperty,
    Mapping,
    Signature,
    SimpleProperty,
    SimpleValue,
    StaticName,
)

from querycat.src.querying.model import VariableId, VariableNameMap
from querycat.src.querying.schema_model import SchemaCategory


class MappingBuilder:
    """Class which builds the mapping which describes the result
    of a native database query corresponding to a single query part.
    """

    def __init__(
        self, schema_category: SchemaCategory, where_schema_category: SchemaCategory
    ):
        self.variable_definitions: Dict[
            VariableId, Tuple[List[AccessPath], Mapping]
        ] = {}
        self.schema_category = schema_category
        self.where_schema_category = where_schema_category

    def define_variable(
        self, variable_id: VariableId, property_path: List[AccessPath], mapping: Mapping
    ) -> None:
        """Make the `MappingBuilder` remember that the `variable_id` is associated
        with a specific property path within a given mapping. This information
        is necessary for when the final mapping is built.
        """
        self.variable_definitions[variable_id] = (property_path, mapping)

    def build_mapping(self, variable_map: VariableNameMap) -> MappingInit:
        """Given a map of variable IDs to names along the corresponding property path,
        build a mapping representing the native result for a single query part.
        """
        root_kind_mapping = list(self.variable_definitions.values())[0][1]
        root_object_key = self.schema_category.get_object(
            root_kind_mapping.root_object_id
        ).key
        new_root_object = self.where_schema_category.get_object_by_key(
            key=root_object_key.value
        )
        mapping_init = MappingInit(
            category_id=self.where_schema_category.id,
            json_value='{"name": "queryPartKind"}',
            mapping_json_value=Mapping(
                pkey=root_kind_mapping.pkey,
                access_path=self._build_access_path(variable_map),
                kind_name=root_kind_mapping.kind_name,
                database=root_kind_mapping.database,
                root_object_id=new_root_object.id,
                root_morphism_id=None,
                category_id=self.where_schema_category.id,
            ).to_mapping_json_value(),
            root_object_id=new_root_object.id,
            database_id=root_kind_mapping.database.id,
        )
        return mapping_init

    def _build_access_path(self, variable_map: VariableNameMap) -> ComplexProperty:
        subpaths = [
            SimpleProperty(
                name=StaticName(value=var_name_path[0]),
                value=SimpleValue(
                    signature=self.variable_definitions[var_id][0][0].value.signature
                ),
            )
            for var_id, var_name_path in variable_map.items()
        ]
        root = ComplexProperty(
            name=StaticName(value="root"),
            signature=Signature(ids=[0], is_null=True),
            subpaths=subpaths,
        )
        return root
