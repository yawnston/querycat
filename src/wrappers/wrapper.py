from dataclasses import dataclass
from typing import List
from querycat.src.open_api_definition_client.models.database_view_type import (
    DatabaseViewType,
)
from querycat.src.querying.mapping_model import ComplexProperty, Mapping


class Operation:
    ...


@dataclass
class Projection(Operation):
    kind_name: str
    property_name: str


class Wrapper:
    _projections: List[Projection]

    def __init__(self):
        self._projections = []

    def add_projection(self, kind_name: str, property_name: str):
        self._projections.append(
            Projection(
                kind_name=kind_name,
                property_name=property_name,
            )
        )

    def add_selection(self):
        pass

    def build_statement(self) -> str:
        raise Exception("Missing implementation of build_statement in wrapper class!")

    def build_access_path(self) -> ComplexProperty:
        raise Exception("Missing implementation of build_access_path in wrapper class!")

    @staticmethod
    def create(mapping: Mapping) -> "Wrapper":
        from querycat.src.wrappers.mongodb_wrapper import MongodbWrapper
        from querycat.src.wrappers.postgresql_wrapper import PostgresqlWrapper

        if mapping.database.type == DatabaseViewType.POSTGRESQL:
            return PostgresqlWrapper()
        if mapping.database.type == DatabaseViewType.MONGODB:
            return MongodbWrapper()
        raise Exception(f"Unknown database type: {mapping.database.type}")
