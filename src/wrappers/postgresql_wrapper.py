from dataclasses import dataclass
from enum import Enum
from typing import Tuple
from querycat.src.querying.model import VariableNameMap
from querycat.src.wrappers.wrapper import Projection, Wrapper


class PostgresqlWrapperError(Exception):
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
        tables = None
        for kind_id, kind_name in self._kinds.items():
            if tables is None:
                tables = kind_name
            else:
                raise PostgresqlWrapperError(
                    "Joining tables is not supported since MM-evocat does not support it!"
                )

        if tables is None:
            raise PostgresqlWrapperError("No tables are selected in FROM clause.")
        return f"FROM {tables}"

    def _build_where(self) -> str:
        where_conditions = ""
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

            if len(where_conditions) > 0:
                where_conditions += " AND "

            where_conditions += f"{var_alias} {native_operator} '{filter.constant}'"

        if not where_conditions:
            return ""

        return f"WHERE {where_conditions}"
