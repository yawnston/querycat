from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.position import Position


T = TypeVar("T", bound="SchemaObjectWrapper")


@attr.s(auto_attribs=True)
class SchemaObjectWrapper:
    """
    Attributes:
        id (Union[Unset, int]):
        json_value (Union[Unset, str]):
        position (Union[Unset, Position]):
    """

    id: Union[Unset, int] = UNSET
    json_value: Union[Unset, str] = UNSET
    position: Union[Unset, "Position"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        json_value = self.json_value
        position: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if json_value is not UNSET:
            field_dict["jsonValue"] = json_value
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.position import Position

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        json_value = d.pop("jsonValue", UNSET)

        _position = d.pop("position", UNSET)
        position: Union[Unset, Position]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = Position.from_dict(_position)

        schema_object_wrapper = cls(
            id=id,
            json_value=json_value,
            position=position,
        )

        schema_object_wrapper.additional_properties = d
        return schema_object_wrapper

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
