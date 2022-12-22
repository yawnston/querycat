from dataclasses import dataclass
from typing import Dict, List
from querycat.src.open_api_definition_client.models.domain_row_view import DomainRowView
from querycat.src.open_api_definition_client.models.instance_morphism_view import (
    InstanceMorphismView,
)
from querycat.src.open_api_definition_client.models.instance_object_view import (
    InstanceObjectView,
)
from querycat.src.open_api_definition_client.models.mapping_row_view import (
    MappingRowView,
)

from querycat.src.querying.mapping_model import Signature
from querycat.src.querying.mmcat_client import MMCat
from querycat.src.querying.schema_model import SchemaCategory


@dataclass
class InstanceObject:
    key: int
    columns: List[Signature]
    rows: List[List[str]]

    @staticmethod
    def from_view(view: InstanceObjectView) -> "InstanceObject":
        return InstanceObject(
            key=view.key.value,
            columns=[Signature.from_view(x) for x in view.columns],
            rows=view.rows,
        )


@dataclass
class InstanceMorphism:
    signature: int
    mappings: List["MappingRow"]

    @staticmethod
    def from_view(signature: int, view: InstanceMorphismView) -> "InstanceMorphism":
        return InstanceMorphism(
            signature=signature,
            mappings=[MappingRow.from_view(x) for x in view.mappings],
        )


@dataclass
class MappingRow:
    domain_row: "DomainRow"
    codomain_row: "DomainRow"

    @staticmethod
    def from_view(view: MappingRowView) -> "MappingRow":
        return MappingRow(
            domain_row=DomainRow.from_view(view.domain_row),
            codomain_row=DomainRow.from_view(view.codomain_row),
        )


@dataclass
class DomainRow:
    tuples: Dict[Signature, str]

    @staticmethod
    def from_view(view: DomainRowView) -> "DomainRow":
        values = view.super_id.tuples.additional_properties.items()

        return DomainRow(
            tuples={
                Signature.from_base_str(signature): value for signature, value in values
            }
        )


class InstanceCategory:
    """Instance Category proxy class, it caches instance objects and morphisms
    which it retrieves from MM-evocat in case they are missing.
    """

    def __init__(self, mmcat: MMCat, schema_category: SchemaCategory):
        self._objects: List[InstanceObject] = []
        self._morphisms: List[InstanceMorphism] = []
        self._mmcat = mmcat
        self.schema_category = schema_category

    def get_object(self, key: int) -> InstanceObject:
        found = next((x for x in self._objects if x.key == key), None)
        if not found:
            found = InstanceObject.from_view(self._mmcat.get_instance_object(key))
            self._objects.append(found)

        return found

    def get_morphism(self, signature: int) -> InstanceMorphism:
        found = next((x for x in self._morphisms if x.signature == signature), None)
        if not found:
            found = InstanceMorphism.from_view(
                self._mmcat.get_instance_morphism(signature)
            )
            self._morphisms.append(found)

        return found
