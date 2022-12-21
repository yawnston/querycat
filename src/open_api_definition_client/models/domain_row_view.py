from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.id_with_values_view import IdWithValuesView


T = TypeVar("T", bound="DomainRowView")


@attr.s(auto_attribs=True)
class DomainRowView:
    """
    Attributes:
        super_id (Union[Unset, IdWithValuesView]):
    """

    super_id: Union[Unset, "IdWithValuesView"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        super_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.super_id, Unset):
            super_id = self.super_id.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if super_id is not UNSET:
            field_dict["superId"] = super_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.id_with_values_view import IdWithValuesView

        d = src_dict.copy()
        _super_id = d.pop("superId", UNSET)
        super_id: Union[Unset, IdWithValuesView]
        if isinstance(_super_id, Unset):
            super_id = UNSET
        else:
            super_id = IdWithValuesView.from_dict(_super_id)

        domain_row_view = cls(
            super_id=super_id,
        )

        domain_row_view.additional_properties = d
        return domain_row_view

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
