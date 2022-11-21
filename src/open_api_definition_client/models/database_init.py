from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.database_init_type import DatabaseInitType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database import Database
    from ..models.database_init_settings import DatabaseInitSettings


T = TypeVar("T", bound="DatabaseInit")


@attr.s(auto_attribs=True)
class DatabaseInit:
    """
    Attributes:
        label (Union[Unset, str]):
        settings (Union[Unset, DatabaseInitSettings]):
        type (Union[Unset, DatabaseInitType]):
        password_from (Union[Unset, Database]):
    """

    label: Union[Unset, str] = UNSET
    settings: Union[Unset, "DatabaseInitSettings"] = UNSET
    type: Union[Unset, DatabaseInitType] = UNSET
    password_from: Union[Unset, "Database"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label
        settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        password_from: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.password_from, Unset):
            password_from = self.password_from.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if settings is not UNSET:
            field_dict["settings"] = settings
        if type is not UNSET:
            field_dict["type"] = type
        if password_from is not UNSET:
            field_dict["passwordFrom"] = password_from

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.database import Database
        from ..models.database_init_settings import DatabaseInitSettings

        d = src_dict.copy()
        label = d.pop("label", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, DatabaseInitSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = DatabaseInitSettings.from_dict(_settings)

        _type = d.pop("type", UNSET)
        type: Union[Unset, DatabaseInitType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DatabaseInitType(_type)

        _password_from = d.pop("passwordFrom", UNSET)
        password_from: Union[Unset, Database]
        if isinstance(_password_from, Unset):
            password_from = UNSET
        else:
            password_from = Database.from_dict(_password_from)

        database_init = cls(
            label=label,
            settings=settings,
            type=type,
            password_from=password_from,
        )

        database_init.additional_properties = d
        return database_init

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
