from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Model")


@attr.s(auto_attribs=True)
class Model:
    """
    Attributes:
        job_id (Union[Unset, int]):
        schema_id (Union[Unset, int]):
        job_name (Union[Unset, str]):
        commands (Union[Unset, str]):
    """

    job_id: Union[Unset, int] = UNSET
    schema_id: Union[Unset, int] = UNSET
    job_name: Union[Unset, str] = UNSET
    commands: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_id = self.job_id
        schema_id = self.schema_id
        job_name = self.job_name
        commands = self.commands

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if schema_id is not UNSET:
            field_dict["schemaId"] = schema_id
        if job_name is not UNSET:
            field_dict["jobName"] = job_name
        if commands is not UNSET:
            field_dict["commands"] = commands

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_id = d.pop("jobId", UNSET)

        schema_id = d.pop("schemaId", UNSET)

        job_name = d.pop("jobName", UNSET)

        commands = d.pop("commands", UNSET)

        model = cls(
            job_id=job_id,
            schema_id=schema_id,
            job_name=job_name,
            commands=commands,
        )

        model.additional_properties = d
        return model

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
