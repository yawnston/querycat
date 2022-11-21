from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.database_type import DatabaseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_settings import DatabaseSettings


T = TypeVar("T", bound="Database")


@attr.s(auto_attribs=True)
class Database:
    """
    Attributes:
        id (Union[Unset, int]):
        type (Union[Unset, DatabaseType]):
        label (Union[Unset, str]):
        settings (Union[Unset, DatabaseSettings]):
    """

    id: Union[Unset, int] = UNSET
    type: Union[Unset, DatabaseType] = UNSET
    label: Union[Unset, str] = UNSET
    settings: Union[Unset, "DatabaseSettings"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        label = self.label
        settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if label is not UNSET:
            field_dict["label"] = label
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.database_settings import DatabaseSettings

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, DatabaseType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DatabaseType(_type)

        label = d.pop("label", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, DatabaseSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = DatabaseSettings.from_dict(_settings)

        database = cls(
            id=id,
            type=type,
            label=label,
            settings=settings,
        )

        database.additional_properties = d
        return database

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
