from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
from querycat.src.open_api_definition_client.models.mapping_init import MappingInit

from querycat.src.parsing.model import Query, Statement, Triple
from querycat.src.querying.mapping_model import Mapping
from querycat.src.querying.schema_model import SchemaObject


@dataclass
class QueryPlan:
    query: Query
    parts: List["QueryPart"]
    deferred_statements: List[Statement]


@dataclass
class JoinPlan:
    ...


@dataclass
class QueryPart:
    triples_mapping: List[Tuple[Triple, "Kind"]]
    statements: List[Statement]
    compiled: Optional["QueryPartCompiled"] = None
    ...

    def get_database(self):
        return self.triples_mapping[0][1].mapping.database


@dataclass
class QueryPartCompiled:
    db_query: str
    mapping_init: MappingInit


@dataclass
class Kind:
    mapping: Mapping
    ...


VariableTypes = Dict[str, SchemaObject]


class InvalidQueryPlanError(Exception):
    pass
