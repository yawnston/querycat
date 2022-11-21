from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_view import DatabaseView


T = TypeVar("T", bound="MappingView")


@attr.s(auto_attribs=True)
class MappingView:
    """
    Attributes:
        id (Union[Unset, int]):
        database_view (Union[Unset, DatabaseView]):
        category_id (Union[Unset, int]):
        root_object_id (Union[Unset, int]):
        root_morphism_id (Union[Unset, int]):
        mapping_json_value (Union[Unset, str]):
        json_value (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    database_view: Union[Unset, "DatabaseView"] = UNSET
    category_id: Union[Unset, int] = UNSET
    root_object_id: Union[Unset, int] = UNSET
    root_morphism_id: Union[Unset, int] = UNSET
    mapping_json_value: Union[Unset, str] = UNSET
    json_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        database_view: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.database_view, Unset):
            database_view = self.database_view.to_dict()

        category_id = self.category_id
        root_object_id = self.root_object_id
        root_morphism_id = self.root_morphism_id
        mapping_json_value = self.mapping_json_value
        json_value = self.json_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if database_view is not UNSET:
            field_dict["databaseView"] = database_view
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
        from ..models.database_view import DatabaseView

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _database_view = d.pop("databaseView", UNSET)
        database_view: Union[Unset, DatabaseView]
        if isinstance(_database_view, Unset):
            database_view = UNSET
        else:
            database_view = DatabaseView.from_dict(_database_view)

        category_id = d.pop("categoryId", UNSET)

        root_object_id = d.pop("rootObjectId", UNSET)

        root_morphism_id = d.pop("rootMorphismId", UNSET)

        mapping_json_value = d.pop("mappingJsonValue", UNSET)

        json_value = d.pop("jsonValue", UNSET)

        mapping_view = cls(
            id=id,
            database_view=database_view,
            category_id=category_id,
            root_object_id=root_object_id,
            root_morphism_id=root_morphism_id,
            mapping_json_value=mapping_json_value,
            json_value=json_value,
        )

        mapping_view.additional_properties = d
        return mapping_view

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
