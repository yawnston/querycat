# Generated from grammars/Querycat.g4 by ANTLR 4.11.1
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .QuerycatParser import QuerycatParser
else:
    from QuerycatParser import QuerycatParser

# This class defines a complete generic visitor for a parse tree produced by QuerycatParser.


class QuerycatVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by QuerycatParser#query.
    def visitQuery(self, ctx: QuerycatParser.QueryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#selectQuery.
    def visitSelectQuery(self, ctx: QuerycatParser.SelectQueryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#selectClause.
    def visitSelectClause(self, ctx: QuerycatParser.SelectClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#selectGraphPattern.
    def visitSelectGraphPattern(self, ctx: QuerycatParser.SelectGraphPatternContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#whereClause.
    def visitWhereClause(self, ctx: QuerycatParser.WhereClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#solutionModifier.
    def visitSolutionModifier(self, ctx: QuerycatParser.SolutionModifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#limitOffsetClauses.
    def visitLimitOffsetClauses(self, ctx: QuerycatParser.LimitOffsetClausesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#orderClause.
    def visitOrderClause(self, ctx: QuerycatParser.OrderClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#orderCondition.
    def visitOrderCondition(self, ctx: QuerycatParser.OrderConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#limitClause.
    def visitLimitClause(self, ctx: QuerycatParser.LimitClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#offsetClause.
    def visitOffsetClause(self, ctx: QuerycatParser.OffsetClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#groupGraphPattern.
    def visitGroupGraphPattern(self, ctx: QuerycatParser.GroupGraphPatternContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#triplesBlock.
    def visitTriplesBlock(self, ctx: QuerycatParser.TriplesBlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#graphPatternNotTriples.
    def visitGraphPatternNotTriples(
        self, ctx: QuerycatParser.GraphPatternNotTriplesContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#optionalGraphPattern.
    def visitOptionalGraphPattern(
        self, ctx: QuerycatParser.OptionalGraphPatternContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#groupOrUnionGraphPattern.
    def visitGroupOrUnionGraphPattern(
        self, ctx: QuerycatParser.GroupOrUnionGraphPatternContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#filter_.
    def visitFilter_(self, ctx: QuerycatParser.Filter_Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#constraint.
    def visitConstraint(self, ctx: QuerycatParser.ConstraintContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#selectTriples.
    def visitSelectTriples(self, ctx: QuerycatParser.SelectTriplesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#triplesSameSubject.
    def visitTriplesSameSubject(self, ctx: QuerycatParser.TriplesSameSubjectContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#propertyListNotEmpty.
    def visitPropertyListNotEmpty(
        self, ctx: QuerycatParser.PropertyListNotEmptyContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#propertyList.
    def visitPropertyList(self, ctx: QuerycatParser.PropertyListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#objectList.
    def visitObjectList(self, ctx: QuerycatParser.ObjectListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#object_.
    def visitObject_(self, ctx: QuerycatParser.Object_Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#verb.
    def visitVerb(self, ctx: QuerycatParser.VerbContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#schemaMorphismOrPath.
    def visitSchemaMorphismOrPath(
        self, ctx: QuerycatParser.SchemaMorphismOrPathContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#schemaMorphism.
    def visitSchemaMorphism(self, ctx: QuerycatParser.SchemaMorphismContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#primaryMorphism.
    def visitPrimaryMorphism(self, ctx: QuerycatParser.PrimaryMorphismContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#dualMorphism.
    def visitDualMorphism(self, ctx: QuerycatParser.DualMorphismContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#graphNode.
    def visitGraphNode(self, ctx: QuerycatParser.GraphNodeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#varOrTerm.
    def visitVarOrTerm(self, ctx: QuerycatParser.VarOrTermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#var_.
    def visitVar_(self, ctx: QuerycatParser.Var_Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#constantTerm.
    def visitConstantTerm(self, ctx: QuerycatParser.ConstantTermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#aggregationTerm.
    def visitAggregationTerm(self, ctx: QuerycatParser.AggregationTermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#distinctModifier.
    def visitDistinctModifier(self, ctx: QuerycatParser.DistinctModifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#aggregationFunc.
    def visitAggregationFunc(self, ctx: QuerycatParser.AggregationFuncContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#expression.
    def visitExpression(self, ctx: QuerycatParser.ExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#conditionalOrExpression.
    def visitConditionalOrExpression(
        self, ctx: QuerycatParser.ConditionalOrExpressionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#conditionalAndExpression.
    def visitConditionalAndExpression(
        self, ctx: QuerycatParser.ConditionalAndExpressionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#valueLogical.
    def visitValueLogical(self, ctx: QuerycatParser.ValueLogicalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#relationalExpression.
    def visitRelationalExpression(
        self, ctx: QuerycatParser.RelationalExpressionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#expressionPart.
    def visitExpressionPart(self, ctx: QuerycatParser.ExpressionPartContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#primaryExpression.
    def visitPrimaryExpression(self, ctx: QuerycatParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#brackettedExpression.
    def visitBrackettedExpression(
        self, ctx: QuerycatParser.BrackettedExpressionContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#numericLiteral.
    def visitNumericLiteral(self, ctx: QuerycatParser.NumericLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#numericLiteralUnsigned.
    def visitNumericLiteralUnsigned(
        self, ctx: QuerycatParser.NumericLiteralUnsignedContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#numericLiteralPositive.
    def visitNumericLiteralPositive(
        self, ctx: QuerycatParser.NumericLiteralPositiveContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#numericLiteralNegative.
    def visitNumericLiteralNegative(
        self, ctx: QuerycatParser.NumericLiteralNegativeContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx: QuerycatParser.BooleanLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#string_.
    def visitString_(self, ctx: QuerycatParser.String_Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QuerycatParser#blankNode.
    def visitBlankNode(self, ctx: QuerycatParser.BlankNodeContext):
        return self.visitChildren(ctx)


del QuerycatParser
