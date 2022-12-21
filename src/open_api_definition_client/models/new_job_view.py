from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewJobView")


@attr.s(auto_attribs=True)
class NewJobView:
    """
    Attributes:
        mapping_id (Union[Unset, int]):
        name (Union[Unset, str]):
        type (Union[Unset, str]):
        query (Union[Unset, str]):
    """

    mapping_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    query: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mapping_id = self.mapping_id
        name = self.name
        type = self.type
        query = self.query

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mapping_id is not UNSET:
            field_dict["mappingId"] = mapping_id
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mapping_id = d.pop("mappingId", UNSET)

        name = d.pop("name", UNSET)

        type = d.pop("type", UNSET)

        query = d.pop("query", UNSET)

        new_job_view = cls(
            mapping_id=mapping_id,
            name=name,
            type=type,
            query=query,
        )

        new_job_view.additional_properties = d
        return new_job_view

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
