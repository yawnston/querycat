from dataclasses import dataclass
from typing import Dict, List, Union
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
    signature: Union[int, str]
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

    def __hash__(self) -> int:
        return hash(tuple(self.tuples))

    @staticmethod
    def from_view(view: DomainRowView) -> "DomainRow":
        values = view.super_id.tuples.additional_properties.items()

        return DomainRow(
            tuples={
                # TODO: the .0 replace is a hack to make MongoDB and PostgreSQL ids compatible
                # It could accidentally change some results somewhere unintentionally.
                Signature.from_base_str(signature): value.replace(".0", "")
                for signature, value in values
            }
        )


class InstanceCategory:
    """Instance Category proxy class, it caches instance objects and morphisms
    which it retrieves from MM-evocat in case they are missing.
    """

    def __init__(self, mmcat: MMCat, schema_category: SchemaCategory):
        self._objects: Dict[int, InstanceObject] = {}
        self._morphisms: Dict[Union[int, str], InstanceMorphism] = {}
        self._mmcat = mmcat
        self.schema_category = schema_category

    def get_object(self, key: int) -> InstanceObject:
        found = self._objects.get(key, None)
        if not found:
            found = InstanceObject.from_view(self._mmcat.get_instance_object(key))
            self._objects[key] = found

        return found

    def get_morphism(self, signature: int) -> InstanceMorphism:
        found = self._morphisms.get(signature, None)
        if not found:
            found = InstanceMorphism.from_view(
                signature=signature, view=self._mmcat.get_instance_morphism(signature)
            )
            self._morphisms[signature] = found

        return found
