import json
from abc import ABC
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional

from querycat.src.open_api_definition_client.models.database_view import DatabaseView
from querycat.src.open_api_definition_client.models.mapping_view import MappingView


class UnknownMappingElementError(Exception):
    pass


@dataclass
class Signature:
    ids: List[int]
    is_null: bool

    @staticmethod
    def from_dict(dict: Dict[str, Any]) -> "Signature":
        return Signature(
            ids=dict["ids"],
            is_null=dict["isNull"],
        )


class NameType(str, Enum):
    STATIC_NAME = "STATIC_NAME"
    ANONYMOUS = "ANONYMOUS"  # Also known as Empty


@dataclass
class Name(ABC):
    @staticmethod
    def from_dict(dict: Dict[str, Any]) -> "Name":
        if dict["_class"] == "StaticName":
            return StaticName(
                type=NameType.STATIC_NAME,
                value=dict["value"],
            )
        if dict["_class"] == "DynamicName":
            return DynamicName(signature=Signature.from_dict(dict["signature"]))

        raise UnknownMappingElementError(dict)


@dataclass
class StaticName(Name):
    value: str
    type: NameType


@dataclass
class DynamicName(Name):
    signature: Signature


@dataclass
class SimpleValue:
    signature: Signature

    @staticmethod
    def from_dict(dict: Dict[str, Any]) -> "SimpleValue":
        return SimpleValue(
            signature=Signature.from_dict(dict["signature"]),
        )


@dataclass
class AccessPath(ABC):
    name: Name
    # value: Union[SimpleValue, "ComplexProperty"]

    def get_property_name(self, morphism: str, accumulator: str) -> Optional[str]:
        ...

    @staticmethod
    def from_dict(dict: Dict[str, Any]) -> "AccessPath":
        if dict["_class"] == "SimpleProperty":
            return SimpleProperty.from_dict(dict)
        elif dict["_class"] == "ComplexProperty":
            return ComplexProperty.from_dict(dict)
        else:
            raise UnknownMappingElementError(dict)


@dataclass
class SimpleProperty(AccessPath):
    value: SimpleValue

    def get_property_name(self, morphism: str, accumulator: str) -> Optional[str]:
        if isinstance(self.name, DynamicName):
            return None  # TODO: dynamic names
        new_accumulator = accumulator + f".{self.name.value}"
        if int(morphism) in self.value.signature.ids:
            return new_accumulator

        return None

    @staticmethod
    def from_dict(dict: Dict[str, Any]) -> "SimpleProperty":
        return SimpleProperty(
            name=Name.from_dict(dict["name"]),
            value=SimpleValue.from_dict(dict["value"]),
        )


@dataclass
class ComplexProperty(AccessPath):
    signature: Signature
    subpaths: List[AccessPath]

    def get_property_name(self, morphism: str, accumulator: str) -> Optional[str]:
        new_accumulator = (accumulator + f".{self.name.value}").strip(
            "."
        )  # TODO: dynamic names
        if int(morphism) in self.signature.ids:
            return new_accumulator

        for subpath in self.subpaths:
            found_property = subpath.get_property_name(morphism, new_accumulator)
            if found_property:
                return found_property

        return None

    @staticmethod
    def from_dict(dict: Dict[str, Any]) -> "ComplexProperty":
        return ComplexProperty(
            name=Name.from_dict(dict["name"]),
            signature=Signature.from_dict(dict["signature"]),
            subpaths=[AccessPath.from_dict(x) for x in dict["subpaths"]],
        )


@dataclass
class Mapping:
    access_path: ComplexProperty
    kind_name: str
    pkey: List[Signature]
    category_id: int
    root_object_id: int
    root_morphism_id: int
    database: DatabaseView

    def get_property_name(self, morphism: str) -> Optional[str]:
        return self.access_path.get_property_name(morphism, accumulator="")

    @staticmethod
    def from_mapping_view(mapping_view: MappingView) -> "Mapping":
        content_dict = json.loads(mapping_view.mapping_json_value)
        return Mapping(
            category_id=mapping_view.category_id,
            root_object_id=mapping_view.root_object_id,
            root_morphism_id=mapping_view.root_morphism_id,
            access_path=AccessPath.from_dict(content_dict["accessPath"]),
            kind_name=content_dict["kindName"],
            pkey=[Signature.from_dict(x) for x in content_dict["pkey"]],
            database=mapping_view.database_view,
        )
