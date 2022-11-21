from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_morphism_update import SchemaMorphismUpdate
    from ..models.schema_object_update import SchemaObjectUpdate


T = TypeVar("T", bound="SchemaCategoryUpdate")


@attr.s(auto_attribs=True)
class SchemaCategoryUpdate:
    """
    Attributes:
        objects (Union[Unset, List['SchemaObjectUpdate']]):
        morphisms (Union[Unset, List['SchemaMorphismUpdate']]):
    """

    objects: Union[Unset, List["SchemaObjectUpdate"]] = UNSET
    morphisms: Union[Unset, List["SchemaMorphismUpdate"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        objects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.objects, Unset):
            objects = []
            for objects_item_data in self.objects:
                objects_item = objects_item_data.to_dict()

                objects.append(objects_item)

        morphisms: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.morphisms, Unset):
            morphisms = []
            for morphisms_item_data in self.morphisms:
                morphisms_item = morphisms_item_data.to_dict()

                morphisms.append(morphisms_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objects is not UNSET:
            field_dict["objects"] = objects
        if morphisms is not UNSET:
            field_dict["morphisms"] = morphisms

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.schema_morphism_update import SchemaMorphismUpdate
        from ..models.schema_object_update import SchemaObjectUpdate

        d = src_dict.copy()
        objects = []
        _objects = d.pop("objects", UNSET)
        for objects_item_data in _objects or []:
            objects_item = SchemaObjectUpdate.from_dict(objects_item_data)

            objects.append(objects_item)

        morphisms = []
        _morphisms = d.pop("morphisms", UNSET)
        for morphisms_item_data in _morphisms or []:
            morphisms_item = SchemaMorphismUpdate.from_dict(morphisms_item_data)

            morphisms.append(morphisms_item)

        schema_category_update = cls(
            objects=objects,
            morphisms=morphisms,
        )

        schema_category_update.additional_properties = d
        return schema_category_update

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
