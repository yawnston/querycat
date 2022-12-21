from dataclasses import dataclass
from typing import Dict, List, Tuple

from querycat.src.parsing.model import Query, Statement, Triple
from querycat.src.querying.mapping_model import Mapping
from querycat.src.querying.schema_model import SchemaObject


@dataclass
class QueryPlan:
    query: Query
    parts: List["QueryPart"]
    # TODO: is the join plan actually needed when evocat is doing the joining?
    # join_plan: "JoinPlan"
    deferred_statements: List[Statement]


@dataclass
class JoinPlan:
    ...


@dataclass
class QueryPart:
    db_query: str
    triples_mapping: List[Tuple[Triple, "Kind"]]
    ...


@dataclass
class Kind:
    mapping: Mapping
    ...


VariableTypes = Dict[str, SchemaObject]


class InvalidQueryPlanError(Exception):
    pass
