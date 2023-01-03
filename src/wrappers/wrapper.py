from abc import ABC
from dataclasses import dataclass
from typing import Dict, List, Tuple
from querycat.src.open_api_definition_client.models.database_view_type import (
    DatabaseViewType,
)
from querycat.src.querying.mapping_model import (
    AccessPath,
    Mapping,
)
from querycat.src.querying.model import KindId, KindName, VariableId, VariableNameMap


class Operation(ABC):
    ...


@dataclass
class Projection(Operation):
    property_path: List[AccessPath]
    kind_id: KindId
    variable_id: VariableId


class Wrapper(ABC):
    """Generic interface for all database wrappers, each of which inherits
    from this class. These wrappers should implement the `build_statement`
    method, which uses the information stored within the wrapper to build
    a native database query for the corresponding database.

    All code should depend on this abstraction, rather than any concrete
    database wrapper.
    """

    _kinds: Dict[KindId, KindName]
    _projections: List[Projection]

    def __init__(self):
        self._kinds = {}
        self._projections = []

    def define_kind(self, kind_id: KindId, kind_name: KindName) -> None:
        self._kinds[kind_id] = kind_name

    def add_projection(
        self, property_path: List[AccessPath], kind_id: KindId, variable_id: VariableId
    ) -> None:
        self._projections.append(
            Projection(
                property_path=property_path, kind_id=kind_id, variable_id=variable_id
            )
        )

    def build_statement(self) -> Tuple[str, VariableNameMap]:
        raise Exception("Missing implementation of build_statement in wrapper class!")

    @staticmethod
    def create(mapping: Mapping) -> "Wrapper":
        from querycat.src.wrappers.mongodb_wrapper import MongodbWrapper
        from querycat.src.wrappers.postgresql_wrapper import PostgresqlWrapper

        if mapping.database.type == DatabaseViewType.POSTGRESQL:
            return PostgresqlWrapper()
        if mapping.database.type == DatabaseViewType.MONGODB:
            return MongodbWrapper()
        raise Exception(f"Unknown database type: {mapping.database.type}")
