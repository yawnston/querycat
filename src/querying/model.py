from dataclasses import dataclass
from typing import Dict, List

from querycat.src.parsing.model import Query, Statement
from querycat.src.querying.schema_model import SchemaObject


@dataclass
class QueryPlan:
    query: Query
    parts: List["QueryPart"]
    join_plan: "JoinPlan"
    deferred_statements: List[Statement]


@dataclass
class JoinPlan:
    ...


@dataclass
class QueryPart:
    ...


@dataclass
class Kind:
    ...


VariableTypes = Dict[str, SchemaObject]
