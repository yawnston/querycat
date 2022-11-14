from typing import List
from antlr4 import *

from querycat.src.querying.antlr_generated.QuerycatVisitor import QuerycatVisitor
from querycat.src.querying.antlr_generated.QuerycatParser import QuerycatParser
from querycat.src.querying.model import (
    Query,
    SelectClause,
    Triple,
    Variable,
    WhereClause,
)


class QueryVisitor(QuerycatVisitor):
    def aggregateResult(self, aggregate, nextResult):
        # TODO: how about aggregating results?
        return nextResult if nextResult is not None else aggregate

    def visitSelectQuery(self, ctx: QuerycatParser.SelectQueryContext):
        select_clause = ctx.selectClause().accept(self)
        where_clause = ctx.whereClause().accept(self)
        variables = (
            select_clause.variables
        )  # TODO: valiadte that variables are the same in SELECT and WHERE
        return Query(select=select_clause, where=where_clause, variables=variables)

    def visitSelectClause(self, ctx: QuerycatParser.SelectClauseContext):
        graph_triples = ctx.selectGraphPattern().selectTriples()
        if graph_triples is not None:
            triples = graph_triples.accept(self)
        else:
            triples = []
        return SelectClause(triples=triples, variables=[])

    def visitWhereClause(self, ctx: QuerycatParser.WhereClauseContext):
        return WhereClause(triples=[], variables=[], filter=None)

    def visitSelectTriples(
        self, ctx: QuerycatParser.SelectTriplesContext
    ) -> List[Triple]:
        same_subject_triples: List[Triple] = ctx.triplesSameSubject().accept(self)
        more_triples_node = ctx.selectTriples()
        if more_triples_node is not None:
            more_triples: List[Triple] = more_triples_node.accept(self)
        else:
            more_triples = []

        return same_subject_triples + more_triples

    def visitTriplesSameSubject(self, ctx: QuerycatParser.TriplesSameSubjectContext):
        var_node = ctx.varOrTerm().var_()
        if var_node is None:
            raise SyntaxError(f"Variable expected in term {ctx.varOrTerm().start}")

        subject = var_node.accept(self)
        morphisms_and_objects = ctx.propertyListNotEmpty().accept(self)
        return [
            Triple(subject=subject, morphism=morphism, object=object)
            for morphism, object in morphisms_and_objects
        ]
    
    def visitPropertyListNotEmpty(self, ctx: QuerycatParser.PropertyListNotEmptyContext):
        verb_nodes = ctx.verb()
        object_nodes = ctx.objectList()

        morphisms_and_objects = []
        for verb_node, object_node in zip(verb_nodes, object_nodes):
            morphism = verb_node.accept(self)
            objects = object_node.accept(self)
            for object in objects:
                morphisms_and_objects.append((morphism, object))
        return morphisms_and_objects

    def visitSchemaMorphismOrPath(self, ctx: QuerycatParser.SchemaMorphismOrPathContext):
        # TODO: compound morphisms
        return ctx.getText()

    def visitObjectList(self, ctx: QuerycatParser.ObjectListContext):
        object_nodes = ctx.object_()
        objects = []
        for object_node in object_nodes:
            object = object_node.accept(self)
            objects.append(object)

        return objects

    def visitVar_(self, ctx: QuerycatParser.Var_Context) -> Variable:
        variable_name_node = ctx.VAR1() or ctx.VAR2()
        variable_name = variable_name_node.symbol.text[1:]
        return Variable(name=variable_name)

    def visitGraphTerm(self, ctx: QuerycatParser.GraphTermContext):
        # TODO: blank nodes, numbers, bools (and strings? missing in grammar so far)
        return ctx.getText()
