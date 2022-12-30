from dataclasses import dataclass
from typing import List
from uuid import uuid4

from querycat.src.parsing.model import Query, Triple, Variable, WhereClause
from querycat.src.querying.utils import (
    get_base_from_dual,
    is_base_morphism,
    is_dual_morphism,
)


@dataclass
class QueryPreprocessor:
    def preprocess_query(self, query: Query) -> Query:
        """Perform preprocessing on the query, according to the algorithm
        presented in the master's thesis.
        """
        where_triples = self._split_compound_morphisms(query.where.triples)
        where_triples = self._reverse_base_morphisms(where_triples)

        where = WhereClause(
            filters=query.where.filters,
            variables=query.where.variables,
            triples=where_triples,
        )
        return Query(
            variables=query.variables,
            select=query.select,
            where=where,
        )

    def _split_compound_morphisms(self, triples: List[Triple]) -> List[Triple]:
        transformed_triples = []

        for triple in triples:
            if is_base_morphism(triple.morphism):
                transformed_triples.append(triple)
            else:
                split_morphisms = triple.morphism.split("/")
                split_triples = [
                    Triple(
                        subject=None,
                        morphism=x,
                        object=None,
                    )
                    for x in split_morphisms
                ]

                split_triples[0].subject = triple.subject
                split_triples[-1].object = triple.object

                for i in range(0, len(split_triples) - 1):
                    new_variable = Variable(name=uuid4().hex)
                    split_triples[i].object = new_variable
                    split_triples[i + 1].subject = new_variable

                transformed_triples.extend(split_triples)

        return transformed_triples

    def _reverse_base_morphisms(self, triples: List[Triple]) -> List[Triple]:
        transformed_triples = []

        for triple in triples:
            if is_base_morphism(triple.morphism):
                if is_dual_morphism(triple.morphism):
                    reverse_triple = Triple(
                        subject=triple.object,
                        morphism=get_base_from_dual(triple.morphism),
                        object=triple.subject,
                    )
                    transformed_triples.append(reverse_triple)
                    continue

            transformed_triples.append(triple)

        return transformed_triples
