from dataclasses import dataclass
from enum import Enum
import json
from typing import Any, Dict, List, Set
from querycat.src.open_api_definition_client.models.schema_category_wrapper import (
    SchemaCategoryWrapper,
)
from querycat.src.open_api_definition_client.models.schema_morphism_wrapper import (
    SchemaMorphismWrapper,
)
from querycat.src.open_api_definition_client.models.schema_object_wrapper import (
    SchemaObjectWrapper,
)

from querycat.src.querying.mapping_model import Signature


class Min(str, Enum):
    ZERO = "ZERO"
    ONE = "ONE"


class Max(str, Enum):
    ONE = "ONE"
    STAR = "STAR"


@dataclass
class Id:
    signatures: List[Signature]

    @staticmethod
    def from_dict(dict: Dict[str, Any]) -> "Id":
        return Id(signatures=[Signature.from_dict(x) for x in dict["signatures"]])


@dataclass
class Key:
    value: int

    @staticmethod
    def from_dict(dict: Dict[str, Any]) -> "Key":
        return Key(value=dict["value"])


@dataclass
class SchemaObject:
    id: int
    key: Key
    label: str
    super_id: Id
    ids: List[Id]

    @staticmethod
    def from_object_view(object: SchemaObjectWrapper) -> "SchemaObject":
        dict = json.loads(object.json_value)
        return SchemaObject(
            id=object.id,
            key=Key.from_dict(dict["key"]),
            label=dict["label"],
            super_id=Id.from_dict(dict["superId"]),
            ids=[Id.from_dict(x) for x in dict["ids"]],
        )


@dataclass
class SchemaMorphism:
    id: int
    signature: Signature
    dom: SchemaObject
    cod: SchemaObject
    min: Min
    max: Max

    @staticmethod
    def from_morphism_view(
        morphism: SchemaMorphismWrapper, objects: List[SchemaObject]
    ) -> "SchemaMorphism":
        dict = json.loads(morphism.json_value)
        return SchemaMorphism(
            id=morphism.id,
            signature=Signature.from_dict(dict["signature"]),
            dom=[x for x in objects if x.id == morphism.dom_id][0],
            cod=[x for x in objects if x.id == morphism.cod_id][0],
            min=dict["min"],
            max=dict["max"],
        )


@dataclass
class SchemaCategory:
    objects: List[SchemaObject]
    morphisms: List[SchemaMorphism]

    @staticmethod
    def from_category_view(schema_category: SchemaCategoryWrapper) -> "SchemaCategory":
        objects = [SchemaObject.from_object_view(x) for x in schema_category.objects]
        return SchemaCategory(
            objects=objects,
            morphisms=[
                SchemaMorphism.from_morphism_view(x, objects)
                for x in schema_category.morphisms
            ],
        )
