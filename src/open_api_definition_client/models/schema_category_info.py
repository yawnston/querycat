from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemaCategoryInfo")


@attr.s(auto_attribs=True)
class SchemaCategoryInfo:
    """
    Attributes:
        id (Union[Unset, int]):
        json_value (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    json_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        json_value = self.json_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if json_value is not UNSET:
            field_dict["jsonValue"] = json_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        json_value = d.pop("jsonValue", UNSET)

        schema_category_info = cls(
            id=id,
            json_value=json_value,
        )

        schema_category_info.additional_properties = d
        return schema_category_info

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
