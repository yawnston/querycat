from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemaMorphismUpdate")


@attr.s(auto_attribs=True)
class SchemaMorphismUpdate:
    """
    Attributes:
        dom_id (Union[Unset, int]):
        cod_id (Union[Unset, int]):
        temporary_dom_id (Union[Unset, int]):
        temporary_cod_id (Union[Unset, int]):
        json_value (Union[Unset, str]):
    """

    dom_id: Union[Unset, int] = UNSET
    cod_id: Union[Unset, int] = UNSET
    temporary_dom_id: Union[Unset, int] = UNSET
    temporary_cod_id: Union[Unset, int] = UNSET
    json_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dom_id = self.dom_id
        cod_id = self.cod_id
        temporary_dom_id = self.temporary_dom_id
        temporary_cod_id = self.temporary_cod_id
        json_value = self.json_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dom_id is not UNSET:
            field_dict["domId"] = dom_id
        if cod_id is not UNSET:
            field_dict["codId"] = cod_id
        if temporary_dom_id is not UNSET:
            field_dict["temporaryDomId"] = temporary_dom_id
        if temporary_cod_id is not UNSET:
            field_dict["temporaryCodId"] = temporary_cod_id
        if json_value is not UNSET:
            field_dict["jsonValue"] = json_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dom_id = d.pop("domId", UNSET)

        cod_id = d.pop("codId", UNSET)

        temporary_dom_id = d.pop("temporaryDomId", UNSET)

        temporary_cod_id = d.pop("temporaryCodId", UNSET)

        json_value = d.pop("jsonValue", UNSET)

        schema_morphism_update = cls(
            dom_id=dom_id,
            cod_id=cod_id,
            temporary_dom_id=temporary_dom_id,
            temporary_cod_id=temporary_cod_id,
            json_value=json_value,
        )

        schema_morphism_update.additional_properties = d
        return schema_morphism_update

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
