from dataclasses import dataclass
from enum import Enum
from typing import List, Union


@dataclass
class Query:
    select: "SelectClause"
    where: "WhereClause"
    variables: List["Variable"]


@dataclass
class SelectClause:
    triples: List["Triple"]
    variables: List["Variable"]


@dataclass
class WhereClause:
    triples: List["Triple"]
    variables: List["Variable"]
    filters: List["Filter"]


class ComparisonOperator(str, Enum):
    EQUALS = "="
    NOT_EQUALS = "!="
    LESS_THAN = "<"
    LESS_THAN_EQUALS = "<="
    GREATER_THAN = ">"
    GREATER_THAN_EQUALS = ">="


@dataclass
class Filter:
    lhs: Union["Variable", str, int]
    operator: ComparisonOperator
    rhs: Union["Variable", str, int]


@dataclass
class Values:
    variable: "Variable"
    allowed_values: List[str]


@dataclass
class Triple:
    subject: "Variable"
    morphism: str
    object: Union["Variable", str]


Statement = Union[Triple, Filter, Values]


@dataclass
class Variable:
    name: str
