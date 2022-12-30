from typing import List

from querycat.src.parsing.antlr_generated.QuerycatParser import QuerycatParser
from querycat.src.parsing.antlr_generated.QuerycatVisitor import QuerycatVisitor
from querycat.src.parsing.model import (
    Filter,
    Query,
    SelectClause,
    Triple,
    Variable,
    WhereClause,
)


class QueryVisitor(QuerycatVisitor):
    """Visitor class whose job is to traverse the AST parsed from each MMQL query,
    and construct the internal query representation which is subsequently processed
    by the rest of the algorithm.
    """

    def aggregateResult(self, aggregate, nextResult):
        # Maybe it would be more convenient to aggregate the results into a tuple or list?
        return nextResult if nextResult is not None else aggregate

    def visitSelectQuery(self, ctx: QuerycatParser.SelectQueryContext):
        select_clause = ctx.selectClause().accept(self)
        where_clause = ctx.whereClause().accept(self)
        variables = select_clause.variables
        return Query(select=select_clause, where=where_clause, variables=variables)

    def visitSelectClause(self, ctx: QuerycatParser.SelectClauseContext):
        graph_triples = ctx.selectGraphPattern().selectTriples()
        if graph_triples is not None:
            triples = graph_triples.accept(self)
        else:
            triples = []
        return SelectClause(triples=triples, variables=[])

    def visitWhereClause(self, ctx: QuerycatParser.WhereClauseContext):
        statements = self.visitGroupGraphPattern(ctx.groupGraphPattern())

        return WhereClause(
            triples=statements[0],
            variables=[],
            filters=statements[1],
        )

    def visitGroupGraphPattern(self, ctx: QuerycatParser.GroupGraphPatternContext):
        triples_lists = [self.visit(x) for x in ctx.triplesBlock()]
        filters = [self.visit(x) for x in ctx.filter_()]
        triples = [triple for list in triples_lists for triple in list]
        return (triples, filters)

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

    def visitTriplesBlock(self, ctx: QuerycatParser.TriplesBlockContext):
        # Almost identical to select triples, but this is necessary as the grammar
        # definition for these constructs is slightly different.
        same_subject_triples: List[Triple] = ctx.triplesSameSubject().accept(self)
        more_triples_node = ctx.triplesBlock()
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

    def visitPropertyListNotEmpty(
        self, ctx: QuerycatParser.PropertyListNotEmptyContext
    ):
        verb_nodes = ctx.verb()
        object_nodes = ctx.objectList()

        morphisms_and_objects = []
        for verb_node, object_node in zip(verb_nodes, object_nodes):
            morphism = verb_node.accept(self)
            objects = object_node.accept(self)
            for object in objects:
                morphisms_and_objects.append((morphism, object))
        return morphisms_and_objects

    def visitSchemaMorphismOrPath(
        self, ctx: QuerycatParser.SchemaMorphismOrPathContext
    ):
        # Should we do the compound morphism parsing here?
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

    def visitString_(self, ctx: QuerycatParser.String_Context):
        return ctx.getText().strip("\"'")

    def visitRelationalExpression(
        self, ctx: QuerycatParser.RelationalExpressionContext
    ):
        children = ctx.children
        if len(children) == 1:
            return self.visit(children[0])

        if len(children) == 3:
            return Filter(
                lhs=self.visit(children[0]),
                operator=ctx.children[1].getText(),
                rhs=self.visit(children[2]),
            )
