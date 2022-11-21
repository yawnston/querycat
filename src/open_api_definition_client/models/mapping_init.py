from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MappingInit")


@attr.s(auto_attribs=True)
class MappingInit:
    """
    Attributes:
        database_id (Union[Unset, int]):
        category_id (Union[Unset, int]):
        root_object_id (Union[Unset, int]):
        root_morphism_id (Union[Unset, int]):
        mapping_json_value (Union[Unset, str]):
        json_value (Union[Unset, str]):
    """

    database_id: Union[Unset, int] = UNSET
    category_id: Union[Unset, int] = UNSET
    root_object_id: Union[Unset, int] = UNSET
    root_morphism_id: Union[Unset, int] = UNSET
    mapping_json_value: Union[Unset, str] = UNSET
    json_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        database_id = self.database_id
        category_id = self.category_id
        root_object_id = self.root_object_id
        root_morphism_id = self.root_morphism_id
        mapping_json_value = self.mapping_json_value
        json_value = self.json_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if database_id is not UNSET:
            field_dict["databaseId"] = database_id
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if root_object_id is not UNSET:
            field_dict["rootObjectId"] = root_object_id
        if root_morphism_id is not UNSET:
            field_dict["rootMorphismId"] = root_morphism_id
        if mapping_json_value is not UNSET:
            field_dict["mappingJsonValue"] = mapping_json_value
        if json_value is not UNSET:
            field_dict["jsonValue"] = json_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        database_id = d.pop("databaseId", UNSET)

        category_id = d.pop("categoryId", UNSET)

        root_object_id = d.pop("rootObjectId", UNSET)

        root_morphism_id = d.pop("rootMorphismId", UNSET)

        mapping_json_value = d.pop("mappingJsonValue", UNSET)

        json_value = d.pop("jsonValue", UNSET)

        mapping_init = cls(
            database_id=database_id,
            category_id=category_id,
            root_object_id=root_object_id,
            root_morphism_id=root_morphism_id,
            mapping_json_value=mapping_json_value,
            json_value=json_value,
        )

        mapping_init.additional_properties = d
        return mapping_init

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
