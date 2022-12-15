from dataclasses import dataclass
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
    filter: None  # TODO: finish the model


@dataclass
class Triple:
    subject: "Variable"
    morphism: str
    object: Union["Variable", str]


@dataclass
class Variable:
    name: str
