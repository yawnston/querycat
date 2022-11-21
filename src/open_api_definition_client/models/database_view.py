from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.database_view_type import DatabaseViewType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_configuration import DatabaseConfiguration


T = TypeVar("T", bound="DatabaseView")


@attr.s(auto_attribs=True)
class DatabaseView:
    """
    Attributes:
        id (Union[Unset, int]):
        type (Union[Unset, DatabaseViewType]):
        label (Union[Unset, str]):
        configuration (Union[Unset, DatabaseConfiguration]):
    """

    id: Union[Unset, int] = UNSET
    type: Union[Unset, DatabaseViewType] = UNSET
    label: Union[Unset, str] = UNSET
    configuration: Union[Unset, "DatabaseConfiguration"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        label = self.label
        configuration: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if label is not UNSET:
            field_dict["label"] = label
        if configuration is not UNSET:
            field_dict["configuration"] = configuration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.database_configuration import DatabaseConfiguration

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, DatabaseViewType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DatabaseViewType(_type)

        label = d.pop("label", UNSET)

        _configuration = d.pop("configuration", UNSET)
        configuration: Union[Unset, DatabaseConfiguration]
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = DatabaseConfiguration.from_dict(_configuration)

        database_view = cls(
            id=id,
            type=type,
            label=label,
            configuration=configuration,
        )

        database_view.additional_properties = d
        return database_view

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
