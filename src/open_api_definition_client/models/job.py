from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.job_status import JobStatus
from ..models.job_type import JobType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Job")


@attr.s(auto_attribs=True)
class Job:
    """
    Attributes:
        id (Union[Unset, int]):
        mapping_id (Union[Unset, int]):
        schema_id (Union[Unset, int]):
        name (Union[Unset, str]):
        type (Union[Unset, JobType]):
        status (Union[Unset, JobStatus]):
        query (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    mapping_id: Union[Unset, int] = UNSET
    schema_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, JobType] = UNSET
    status: Union[Unset, JobStatus] = UNSET
    query: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        mapping_id = self.mapping_id
        schema_id = self.schema_id
        name = self.name
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        query = self.query

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if mapping_id is not UNSET:
            field_dict["mappingId"] = mapping_id
        if schema_id is not UNSET:
            field_dict["schemaId"] = schema_id
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if status is not UNSET:
            field_dict["status"] = status
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        mapping_id = d.pop("mappingId", UNSET)

        schema_id = d.pop("schemaId", UNSET)

        name = d.pop("name", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, JobType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = JobType(_type)

        _status = d.pop("status", UNSET)
        status: Union[Unset, JobStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = JobStatus(_status)

        query = d.pop("query", UNSET)

        job = cls(
            id=id,
            mapping_id=mapping_id,
            schema_id=schema_id,
            name=name,
            type=type,
            status=status,
            query=query,
        )

        job.additional_properties = d
        return job

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
