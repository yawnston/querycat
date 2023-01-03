from abc import ABC
from dataclasses import dataclass
from typing import Dict, List, Tuple
from querycat.src.open_api_definition_client.models.database_view_type import (
    DatabaseViewType,
)
from querycat.src.parsing.model import ComparisonOperator
from querycat.src.querying.mapping_model import (
    AccessPath,
    Mapping,
)
from querycat.src.querying.model import KindId, KindName, VariableId, VariableNameMap


class WrapperError(Exception):
    """Base class for all errors emitted from wrappers."""

    pass


class Operation(ABC):
    """Base class for all operations which can be stored by the wrapper."""

    ...


@dataclass
class Projection(Operation):
    """Operation corresponding to projection of a property,
    as defined by graph patterns in MMQL.
    """

    property_path: List[AccessPath]
    kind_id: KindId
    variable_id: VariableId


@dataclass
class ConstantFilter(Operation):
    """Operation corresponding to a MMQL `FILTER` statement
    of the form `FILTER(?var op constant).
    """

    variable_id: VariableId
    operator: ComparisonOperator
    constant: str


@dataclass
class VariablesFilter(Operation):
    """Operation corresponding to a MMQL `FILTER` statement
    of the form `FILTER(?var1 op ?var2)`."""

    lhs_variable_id: VariableId
    operator: ComparisonOperator
    rhs_variable_id: VariableId


@dataclass
class ValuesFilter(Operation):
    """Operation corresponding to a MMQL `VALUES` statement
    of the form `VALUES ?var {constant1, constant2}`."""

    variable_id: VariableId
    constants: List[str]


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
    _constant_filters: List[ConstantFilter]
    _variables_filters: List[VariablesFilter]
    _values_filters: List[ValuesFilter]

    def __init__(self):
        self._kinds = {}
        self._projections = []
        self._constant_filters = []
        self._variables_filters = []
        self._values_filters = []

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

    def add_constant_filter(
        self, variable_id: VariableId, operator: ComparisonOperator, constant: str
    ) -> None:
        self._constant_filters.append(
            ConstantFilter(
                variable_id=variable_id, operator=operator, constant=constant
            )
        )

    def add_variables_filter(
        self,
        lhs_variable_id: VariableId,
        operator: ComparisonOperator,
        rhs_variable_id: VariableId,
    ) -> None:
        self._variables_filters.append(
            VariablesFilter(
                lhs_variable_id=lhs_variable_id,
                operator=operator,
                rhs_variable_id=rhs_variable_id,
            )
        )

    def add_values_filter(self, variable_id: VariableId, constants: List[str]) -> None:
        self._values_filters.append(
            ValuesFilter(variable_id=variable_id, constants=constants)
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
