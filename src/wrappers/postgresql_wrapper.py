from dataclasses import dataclass
from enum import Enum
from typing import Tuple
from querycat.src.querying.model import VariableNameMap
from querycat.src.wrappers.wrapper import Projection, Wrapper, WrapperError


class PostgresqlWrapperError(WrapperError):
    pass


class PostgresqlComparisonOperator(str, Enum):
    EQUALS = "="
    NOT_EQUALS = "<>"
    LESS_THAN = "<"
    LESS_THAN_EQUALS = "<="
    GREATER_THAN = ">"
    GREATER_THAN_EQUALS = ">="


@dataclass
class PostgresqlWrapper(Wrapper):
    def __init__(self):
        super().__init__()

    def is_join_supported(self) -> bool:
        return True

    def is_optional_join_supported(self) -> bool:
        return True

    def is_non_id_filter_supported(self) -> bool:
        return True

    def build_statement(self) -> Tuple[str, VariableNameMap]:
        query, var_name_map = self._build_select()
        query += f" {self._build_from()}"
        query += f" {self._build_where()}"
        return query, var_name_map

    def _build_select(self) -> Tuple[str, VariableNameMap]:
        var_selections = [
            self._get_var_alias(projection) for projection in self._projections
        ]
        var_name_map = {
            x.variable_id: [self._get_var_name(x)] for x in self._projections
        }

        select = f"SELECT {', '.join(var_selections)}"
        return select, var_name_map

    def _get_var_selection(self, projection: Projection) -> str:
        return f"{self._kinds[projection.kind_id]}.{projection.property_path[-1].name.value}"

    def _get_var_alias(self, projection: Projection) -> str:
        selection = self._get_var_selection(projection)
        alias = self._get_var_name(projection)
        return f"{selection} AS {alias}"

    def _get_var_name(self, projection: Projection) -> str:
        return f"{self._kinds[projection.kind_id]}_{projection.property_path[-1].name.value}"

    def _build_from(self) -> str:
        if not self._joins:
            table = next(iter(self._kinds.values()), None)
            if table is None:
                raise PostgresqlWrapperError("No tables are selected in FROM clause.")

            return f"FROM {table}"

        joined_kind_ids = []
        joined_tables = ""
        for join in self._joins:
            ...

        return f"FROM {joined_tables}"

    def _build_where(self) -> str:
        filters = self._build_filters()
        values_filters = self._build_values()

        if filters and values_filters:
            where_conditions = f"{filters} AND {values_filters}"
        else:
            where_conditions = filters or values_filters

        if not where_conditions:
            return ""

        return f"WHERE {where_conditions}"

    def _build_filters(self) -> str:
        filters = []
        for filter in self._constant_filters:
            # We can't use the variable name since in SQL, we cannot use an alias
            # in the WHERE clause.
            var_alias = self._get_var_selection(
                [x for x in self._projections if x.variable_id == filter.variable_id][0]
            )

            operator_name = filter.operator.name
            if not operator_name in PostgresqlComparisonOperator.__members__:
                raise PostgresqlWrapperError(
                    f"Comparison operator {filter.operator} is not supported by PostgreSQL!"
                )
            native_operator = PostgresqlComparisonOperator[operator_name].value

            filters.append(f"{var_alias} {native_operator} '{filter.constant}'")

        for filter in self._variables_filters:
            lhs_var_alias = self._get_var_selection(
                [
                    x
                    for x in self._projections
                    if x.variable_id == filter.lhs_variable_id
                ][0]
            )
            rhs_var_alias = self._get_var_selection(
                [
                    x
                    for x in self._projections
                    if x.variable_id == filter.rhs_variable_id
                ][0]
            )

            operator_name = filter.operator.name
            if not operator_name in PostgresqlComparisonOperator.__members__:
                raise PostgresqlWrapperError(
                    f"Comparison operator {filter.operator} is not supported by PostgreSQL!"
                )
            native_operator = PostgresqlComparisonOperator[operator_name].value

            filters.append(f"{lhs_var_alias} {native_operator} {rhs_var_alias}")

        return " AND ".join(filters)

    def _build_values(self) -> str:
        values_filters = []
        for values in self._values_filters:
            var_alias = self._get_var_selection(
                [x for x in self._projections if x.variable_id == values.variable_id][0]
            )

            if not values.constants:
                raise PostgresqlWrapperError(
                    f"VALUES clause for variable {var_alias} has no allowed values."
                )

            sql_value_strings = [f"'{x}'" for x in values.constants]
            values_filters.append(f"{var_alias} IN ({','.join(sql_value_strings)})")

        return " AND ".join(values_filters)
