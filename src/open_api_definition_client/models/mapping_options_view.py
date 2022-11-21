from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database import Database


T = TypeVar("T", bound="MappingOptionsView")


@attr.s(auto_attribs=True)
class MappingOptionsView:
    """
    Attributes:
        category_id (Union[Unset, int]):
        databases (Union[Unset, List['Database']]):
    """

    category_id: Union[Unset, int] = UNSET
    databases: Union[Unset, List["Database"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category_id = self.category_id
        databases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.databases, Unset):
            databases = []
            for databases_item_data in self.databases:
                databases_item = databases_item_data.to_dict()

                databases.append(databases_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if databases is not UNSET:
            field_dict["databases"] = databases

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.database import Database

        d = src_dict.copy()
        category_id = d.pop("categoryId", UNSET)

        databases = []
        _databases = d.pop("databases", UNSET)
        for databases_item_data in _databases or []:
            databases_item = Database.from_dict(databases_item_data)

            databases.append(databases_item)

        mapping_options_view = cls(
            category_id=category_id,
            databases=databases,
        )

        mapping_options_view.additional_properties = d
        return mapping_options_view

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
