from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_morphism_wrapper import SchemaMorphismWrapper
    from ..models.schema_object_wrapper import SchemaObjectWrapper


T = TypeVar("T", bound="SchemaCategoryWrapper")


@attr.s(auto_attribs=True)
class SchemaCategoryWrapper:
    """
    Attributes:
        id (Union[Unset, int]):
        json_value (Union[Unset, str]):
        objects (Union[Unset, List['SchemaObjectWrapper']]):
        morphisms (Union[Unset, List['SchemaMorphismWrapper']]):
    """

    id: Union[Unset, int] = UNSET
    json_value: Union[Unset, str] = UNSET
    objects: Union[Unset, List["SchemaObjectWrapper"]] = UNSET
    morphisms: Union[Unset, List["SchemaMorphismWrapper"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        json_value = self.json_value
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
        if id is not UNSET:
            field_dict["id"] = id
        if json_value is not UNSET:
            field_dict["jsonValue"] = json_value
        if objects is not UNSET:
            field_dict["objects"] = objects
        if morphisms is not UNSET:
            field_dict["morphisms"] = morphisms

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.schema_morphism_wrapper import SchemaMorphismWrapper
        from ..models.schema_object_wrapper import SchemaObjectWrapper

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        json_value = d.pop("jsonValue", UNSET)

        objects = []
        _objects = d.pop("objects", UNSET)
        for objects_item_data in _objects or []:
            objects_item = SchemaObjectWrapper.from_dict(objects_item_data)

            objects.append(objects_item)

        morphisms = []
        _morphisms = d.pop("morphisms", UNSET)
        for morphisms_item_data in _morphisms or []:
            morphisms_item = SchemaMorphismWrapper.from_dict(morphisms_item_data)

            morphisms.append(morphisms_item)

        schema_category_wrapper = cls(
            id=id,
            json_value=json_value,
            objects=objects,
            morphisms=morphisms,
        )

        schema_category_wrapper.additional_properties = d
        return schema_category_wrapper

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
