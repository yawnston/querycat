from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_row_view import DomainRowView


T = TypeVar("T", bound="MappingRowView")


@attr.s(auto_attribs=True)
class MappingRowView:
    """
    Attributes:
        domain_row (Union[Unset, DomainRowView]):
        codomain_row (Union[Unset, DomainRowView]):
    """

    domain_row: Union[Unset, "DomainRowView"] = UNSET
    codomain_row: Union[Unset, "DomainRowView"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        domain_row: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.domain_row, Unset):
            domain_row = self.domain_row.to_dict()

        codomain_row: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.codomain_row, Unset):
            codomain_row = self.codomain_row.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain_row is not UNSET:
            field_dict["domainRow"] = domain_row
        if codomain_row is not UNSET:
            field_dict["codomainRow"] = codomain_row

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_row_view import DomainRowView

        d = src_dict.copy()
        _domain_row = d.pop("domainRow", UNSET)
        domain_row: Union[Unset, DomainRowView]
        if isinstance(_domain_row, Unset):
            domain_row = UNSET
        else:
            domain_row = DomainRowView.from_dict(_domain_row)

        _codomain_row = d.pop("codomainRow", UNSET)
        codomain_row: Union[Unset, DomainRowView]
        if isinstance(_codomain_row, Unset):
            codomain_row = UNSET
        else:
            codomain_row = DomainRowView.from_dict(_codomain_row)

        mapping_row_view = cls(
            domain_row=domain_row,
            codomain_row=codomain_row,
        )

        mapping_row_view.additional_properties = d
        return mapping_row_view

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
