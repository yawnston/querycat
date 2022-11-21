from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.key_view import KeyView
    from ..models.signature_view import SignatureView


T = TypeVar("T", bound="InstanceObjectView")


@attr.s(auto_attribs=True)
class InstanceObjectView:
    """
    Attributes:
        key (Union[Unset, KeyView]):
        columns (Union[Unset, List['SignatureView']]):
        rows (Union[Unset, List[List[str]]]):
    """

    key: Union[Unset, "KeyView"] = UNSET
    columns: Union[Unset, List["SignatureView"]] = UNSET
    rows: Union[Unset, List[List[str]]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.to_dict()

        columns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.columns, Unset):
            columns = []
            for columns_item_data in self.columns:
                columns_item = columns_item_data.to_dict()

                columns.append(columns_item)

        rows: Union[Unset, List[List[str]]] = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data

                rows.append(rows_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if columns is not UNSET:
            field_dict["columns"] = columns
        if rows is not UNSET:
            field_dict["rows"] = rows

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.key_view import KeyView
        from ..models.signature_view import SignatureView

        d = src_dict.copy()
        _key = d.pop("key", UNSET)
        key: Union[Unset, KeyView]
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = KeyView.from_dict(_key)

        columns = []
        _columns = d.pop("columns", UNSET)
        for columns_item_data in _columns or []:
            columns_item = SignatureView.from_dict(columns_item_data)

            columns.append(columns_item)

        rows = []
        _rows = d.pop("rows", UNSET)
        for rows_item_data in _rows or []:
            rows_item = cast(List[str], rows_item_data)

            rows.append(rows_item)

        instance_object_view = cls(
            key=key,
            columns=columns,
            rows=rows,
        )

        instance_object_view.additional_properties = d
        return instance_object_view

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
