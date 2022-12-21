from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.id_with_values_view_tuples import IdWithValuesViewTuples


T = TypeVar("T", bound="IdWithValuesView")


@attr.s(auto_attribs=True)
class IdWithValuesView:
    """
    Attributes:
        tuples (Union[Unset, IdWithValuesViewTuples]):
    """

    tuples: Union[Unset, "IdWithValuesViewTuples"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tuples: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tuples, Unset):
            tuples = self.tuples.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tuples is not UNSET:
            field_dict["tuples"] = tuples

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.id_with_values_view_tuples import IdWithValuesViewTuples

        d = src_dict.copy()
        _tuples = d.pop("tuples", UNSET)
        tuples: Union[Unset, IdWithValuesViewTuples]
        if isinstance(_tuples, Unset):
            tuples = UNSET
        else:
            tuples = IdWithValuesViewTuples.from_dict(_tuples)

        id_with_values_view = cls(
            tuples=tuples,
        )

        id_with_values_view.additional_properties = d
        return id_with_values_view

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
