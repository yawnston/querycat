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

    def get_root_var(self) -> "Variable":
        """Get root variable of the SELECT clause."""
        for var in [x.subject for x in self.triples]:
            if not any(x.object == var for x in self.triples):
                return var

        raise Exception("Cannot determine root variable of SELECT clause")


@dataclass
class WhereClause:
    triples: List["Triple"]
    variables: List["Variable"]
    filters: List["Filter"]
    values: List["Values"]


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
