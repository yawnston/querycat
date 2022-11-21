from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseConfiguration")


@attr.s(auto_attribs=True)
class DatabaseConfiguration:
    """
    Attributes:
        is_property_to_one_allowed (Union[Unset, bool]):
        is_property_to_many_allowed (Union[Unset, bool]):
        is_inlining_to_one_allowed (Union[Unset, bool]):
        is_inlining_to_many_allowed (Union[Unset, bool]):
        is_groupping_allowed (Union[Unset, bool]):
        is_dynamic_naming_allowed (Union[Unset, bool]):
        is_anonymous_naming_allowed (Union[Unset, bool]):
        is_reference_allowed (Union[Unset, bool]):
        is_complex_property_allowed (Union[Unset, bool]):
    """

    is_property_to_one_allowed: Union[Unset, bool] = UNSET
    is_property_to_many_allowed: Union[Unset, bool] = UNSET
    is_inlining_to_one_allowed: Union[Unset, bool] = UNSET
    is_inlining_to_many_allowed: Union[Unset, bool] = UNSET
    is_groupping_allowed: Union[Unset, bool] = UNSET
    is_dynamic_naming_allowed: Union[Unset, bool] = UNSET
    is_anonymous_naming_allowed: Union[Unset, bool] = UNSET
    is_reference_allowed: Union[Unset, bool] = UNSET
    is_complex_property_allowed: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_property_to_one_allowed = self.is_property_to_one_allowed
        is_property_to_many_allowed = self.is_property_to_many_allowed
        is_inlining_to_one_allowed = self.is_inlining_to_one_allowed
        is_inlining_to_many_allowed = self.is_inlining_to_many_allowed
        is_groupping_allowed = self.is_groupping_allowed
        is_dynamic_naming_allowed = self.is_dynamic_naming_allowed
        is_anonymous_naming_allowed = self.is_anonymous_naming_allowed
        is_reference_allowed = self.is_reference_allowed
        is_complex_property_allowed = self.is_complex_property_allowed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_property_to_one_allowed is not UNSET:
            field_dict["isPropertyToOneAllowed"] = is_property_to_one_allowed
        if is_property_to_many_allowed is not UNSET:
            field_dict["isPropertyToManyAllowed"] = is_property_to_many_allowed
        if is_inlining_to_one_allowed is not UNSET:
            field_dict["isInliningToOneAllowed"] = is_inlining_to_one_allowed
        if is_inlining_to_many_allowed is not UNSET:
            field_dict["isInliningToManyAllowed"] = is_inlining_to_many_allowed
        if is_groupping_allowed is not UNSET:
            field_dict["isGrouppingAllowed"] = is_groupping_allowed
        if is_dynamic_naming_allowed is not UNSET:
            field_dict["isDynamicNamingAllowed"] = is_dynamic_naming_allowed
        if is_anonymous_naming_allowed is not UNSET:
            field_dict["isAnonymousNamingAllowed"] = is_anonymous_naming_allowed
        if is_reference_allowed is not UNSET:
            field_dict["isReferenceAllowed"] = is_reference_allowed
        if is_complex_property_allowed is not UNSET:
            field_dict["isComplexPropertyAllowed"] = is_complex_property_allowed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_property_to_one_allowed = d.pop("isPropertyToOneAllowed", UNSET)

        is_property_to_many_allowed = d.pop("isPropertyToManyAllowed", UNSET)

        is_inlining_to_one_allowed = d.pop("isInliningToOneAllowed", UNSET)

        is_inlining_to_many_allowed = d.pop("isInliningToManyAllowed", UNSET)

        is_groupping_allowed = d.pop("isGrouppingAllowed", UNSET)

        is_dynamic_naming_allowed = d.pop("isDynamicNamingAllowed", UNSET)

        is_anonymous_naming_allowed = d.pop("isAnonymousNamingAllowed", UNSET)

        is_reference_allowed = d.pop("isReferenceAllowed", UNSET)

        is_complex_property_allowed = d.pop("isComplexPropertyAllowed", UNSET)

        database_configuration = cls(
            is_property_to_one_allowed=is_property_to_one_allowed,
            is_property_to_many_allowed=is_property_to_many_allowed,
            is_inlining_to_one_allowed=is_inlining_to_one_allowed,
            is_inlining_to_many_allowed=is_inlining_to_many_allowed,
            is_groupping_allowed=is_groupping_allowed,
            is_dynamic_naming_allowed=is_dynamic_naming_allowed,
            is_anonymous_naming_allowed=is_anonymous_naming_allowed,
            is_reference_allowed=is_reference_allowed,
            is_complex_property_allowed=is_complex_property_allowed,
        )

        database_configuration.additional_properties = d
        return database_configuration

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
