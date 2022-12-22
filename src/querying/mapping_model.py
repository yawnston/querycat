import json
from abc import ABC
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from querycat.src.open_api_definition_client.models.database_view import DatabaseView
from querycat.src.open_api_definition_client.models.mapping_view import MappingView
from querycat.src.open_api_definition_client.models.signature_view import SignatureView


class UnknownMappingElementError(Exception):
    pass


@dataclass
class Signature:
    ids: List[Union[int, str]]
    is_null: bool

    def __hash__(self) -> int:
        return hash(tuple(self.ids))

    @staticmethod
    def from_view(view: SignatureView) -> "Signature":
        return Signature(
            ids=view.ids,
            is_null=view.is_null,
        )

    @staticmethod
    def from_base_str(s: str) -> "Signature":
        if s == "_EMPTY":
            return Signature(ids=[], is_null=False)

        return Signature(ids=[int(s)], is_null=False)

    @staticmethod
    def from_dict(dict: Dict[str, Any]) -> "Signature":
        return Signature(
            ids=dict["ids"],
            is_null=dict["isNull"],
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ids": self.ids,
            "isNull": self.is_null,
        }


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

    def to_dict(self) -> Dict[str, Any]:
        ...


@dataclass
class StaticName(Name):
    value: str
    type: NameType = NameType.STATIC_NAME

    def to_dict(self) -> Dict[str, Any]:
        return {
            "value": self.value,
            "_class": "StaticName",
            "type": self.type,
        }


@dataclass
class DynamicName(Name):
    signature: Signature

    def to_dict(self) -> Dict[str, Any]:
        return {
            "signature": self.signature.to_dict(),
            "_class": "DynamicName",
        }


@dataclass
class SimpleValue:
    signature: Signature

    @staticmethod
    def from_dict(dict: Dict[str, Any]) -> "SimpleValue":
        return SimpleValue(
            signature=Signature.from_dict(dict["signature"]),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "signature": self.signature.to_dict(),
        }


@dataclass
class AccessPath(ABC):
    name: Name
    # value: Union[SimpleValue, "ComplexProperty"]

    def get_property_name(self, morphism: str, accumulator: str) -> Optional[str]:
        ...

    def to_dict(self) -> Dict[str, Any]:
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

    def get_signature(
        self, morphism: str, accumulator: List[int]
    ) -> Optional[List[int]]:
        new_accumulator = self.value.signature.ids + accumulator
        # TODO: compound morphisms? we should trim this somehow
        if int(morphism) in self.value.signature.ids:
            return new_accumulator

        return None

    @staticmethod
    def from_dict(dict: Dict[str, Any]) -> "SimpleProperty":
        return SimpleProperty(
            name=Name.from_dict(dict["name"]),
            value=SimpleValue.from_dict(dict["value"]),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "_class": "SimpleProperty",
            "name": self.name.to_dict(),
            "value": self.value.to_dict(),
        }


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

    def get_signature(
        self, morphism: str, accumulator: List[int]
    ) -> Optional[List[int]]:
        if not self.signature.is_null:
            new_accumulator = self.signature.ids + accumulator
        else:
            new_accumulator = accumulator
        if int(morphism) in self.signature.ids:
            # TODO: what if it's for example the 2 in 1.2.3: {...}
            return new_accumulator

        for subpath in self.subpaths:
            found_signature = subpath.get_signature(morphism, new_accumulator)
            if found_signature:
                return found_signature

        return None

    @staticmethod
    def from_dict(dict: Dict[str, Any]) -> "ComplexProperty":
        return ComplexProperty(
            name=Name.from_dict(dict["name"]),
            signature=Signature.from_dict(dict["signature"]),
            subpaths=[AccessPath.from_dict(x) for x in dict["subpaths"]],
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "_class": "ComplexProperty",
            "name": self.name.to_dict(),
            "signature": self.signature.to_dict(),
            "subpaths": [x.to_dict() for x in self.subpaths],
        }


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
        full_name = self.access_path.get_property_name(morphism, accumulator="")
        if full_name is None:
            return None

        # Remove the root kind part
        return ".".join(full_name.split(".")[1:])

    def get_signature(self, morphism: str) -> Optional[Signature]:
        signature_ids = self.access_path.get_signature(morphism, accumulator=[])
        if signature_ids is None:
            return None

        return Signature(
            ids=signature_ids,
            is_null=False,
        )

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

    def to_mapping_json_value(self) -> str:
        dict = {
            "pkey": [x.to_dict() for x in self.pkey],
            "kindName": self.kind_name,
            "accessPath": self.access_path.to_dict(),
        }

        return json.dumps(dict)
