from dataclasses import dataclass
from querycat.src.querying.mapping_model import (
    ComplexProperty,
    Mapping,
    Signature,
    SimpleProperty,
    SimpleValue,
    StaticName,
)
from querycat.src.wrappers.wrapper import Projection, Wrapper


class PostgresqlWrapperError(Exception):
    pass


@dataclass
class PostgresqlWrapper(Wrapper):
    def __init__(self):
        super().__init__()

    def build_statement(self) -> str:
        query = self._build_select()
        query += f" {self._build_from()}"
        return query

    def _build_select(self) -> str:
        var_selections = [
            self._get_var_alias(projection) for projection in self._projections
        ]
        return f"SELECT {', '.join(var_selections)}"

    def _get_var_alias(self, projection: Projection) -> str:
        selection = f"{projection.kind_name}.{projection.property_name}"
        alias = self._get_var_name(projection)
        return f"{selection} AS {alias}"

    def _get_var_name(self, projection: Projection) -> str:
        return f"{projection.kind_name}_{projection.property_name}"

    def _build_from(self) -> str:
        # TODO: joins
        tables = None
        kind_names = {projection.kind_name for projection in self._projections}
        for kind_name in kind_names:
            if tables is None:
                tables = kind_name
            else:
                raise Exception("Joining tables is not yet implemented!")

        if tables is None:
            raise PostgresqlWrapperError("No tables are selected in FROM clause.")
        return f"FROM {tables}"

    def build_access_path(self) -> ComplexProperty:
        # TODO: refactor this to have a separate PathBuilder object (not in the wrapper)
        # TODO: more complex access paths, joins
        subpaths = [
            SimpleProperty(
                name=StaticName(value=self._get_var_name(projection)),
                value=SimpleValue(signature=projection.signature),
            )
            for projection in self._projections
        ]
        root = ComplexProperty(
            name=StaticName(value="root"),
            signature=Signature(ids=[0], is_null=True),
            subpaths=subpaths,
        )
        return root
