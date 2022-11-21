from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database import Database
    from ..models.database_update_settings import DatabaseUpdateSettings


T = TypeVar("T", bound="DatabaseUpdate")


@attr.s(auto_attribs=True)
class DatabaseUpdate:
    """
    Attributes:
        label (Union[Unset, str]):
        settings (Union[Unset, DatabaseUpdateSettings]):
        password_from (Union[Unset, Database]):
    """

    label: Union[Unset, str] = UNSET
    settings: Union[Unset, "DatabaseUpdateSettings"] = UNSET
    password_from: Union[Unset, "Database"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label
        settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

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
        if password_from is not UNSET:
            field_dict["passwordFrom"] = password_from

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.database import Database
        from ..models.database_update_settings import DatabaseUpdateSettings

        d = src_dict.copy()
        label = d.pop("label", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, DatabaseUpdateSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = DatabaseUpdateSettings.from_dict(_settings)

        _password_from = d.pop("passwordFrom", UNSET)
        password_from: Union[Unset, Database]
        if isinstance(_password_from, Unset):
            password_from = UNSET
        else:
            password_from = Database.from_dict(_password_from)

        database_update = cls(
            label=label,
            settings=settings,
            password_from=password_from,
        )

        database_update.additional_properties = d
        return database_update

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
