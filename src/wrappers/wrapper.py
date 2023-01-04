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


JoinProperties = List[Tuple[List[AccessPath], List[AccessPath]]]


@dataclass
class Join(Operation):
    """Operation corresponding to an inner join between the
    two specified kinds on the specified properties.

    The `join_properties` contains a list of tuples, each of which
    contains a property path from the left kind, meaning that this
    property should be inner joined on equality to the corresponding
    property from the right kind.
    """

    lhs_kind_id: KindId
    join_properties: JoinProperties
    rhs_kind_id: KindId


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
    _joins: List[Join]

    def __init__(self):
        self._kinds = {}
        self._projections = []
        self._constant_filters = []
        self._variables_filters = []
        self._values_filters = []
        self._joins = []

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

    def add_join(
        self, lhs_kind_id: KindId, join_properties: JoinProperties, rhs_kind_id: KindId
    ) -> None:
        self._joins.append(
            Join(
                lhs_kind_id=lhs_kind_id,
                join_properties=join_properties,
                rhs_kind_id=rhs_kind_id,
            )
        )

    def build_statement(self) -> Tuple[str, VariableNameMap]:
        """Build the native query using this wrapper, returning a tuple
        `(native_query, variable_name_map)` where `native_query` is the compiled
        native database query, and `variable_name_map` maps variable identifiers
        to final name paths within the native query result.
        """
        raise Exception("Missing implementation of build_statement in wrapper class!")

    def is_join_supported(self) -> bool:
        """Defines whether non-optional (inner) joins are supported."""
        raise Exception("Missing implementation of is_join_supported in wrapper class!")

    def is_optional_join_supported(self) -> bool:
        """Defines whether optional (left outer) joins are supported."""
        raise Exception(
            "Missing implementation of is_optional_join_supported in wrapper class!"
        )

    def is_non_id_filter_supported(self) -> bool:
        """Defines whether it is possible to filter on properties which are not
        in an object's ids."""
        raise Exception(
            "Missing implementation of is_non_id_filter_supported in wrapper class!"
        )

    @staticmethod
    def create(mapping: Mapping) -> "Wrapper":
        """Factory method for wrappers which constructs a wrapper for the mapping's
        corresponding database.
        """
        from querycat.src.wrappers.mongodb_wrapper import MongodbWrapper
        from querycat.src.wrappers.postgresql_wrapper import PostgresqlWrapper

        if mapping.database.type == DatabaseViewType.POSTGRESQL:
            return PostgresqlWrapper()
        if mapping.database.type == DatabaseViewType.MONGODB:
            return MongodbWrapper()
        raise Exception(f"Unknown database type: {mapping.database.type}")
