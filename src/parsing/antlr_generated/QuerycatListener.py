# Generated from grammars/Querycat.g4 by ANTLR 4.11.1
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .QuerycatParser import QuerycatParser
else:
    from QuerycatParser import QuerycatParser

# This class defines a complete listener for a parse tree produced by QuerycatParser.
class QuerycatListener(ParseTreeListener):

    # Enter a parse tree produced by QuerycatParser#query.
    def enterQuery(self, ctx: QuerycatParser.QueryContext):
        pass

    # Exit a parse tree produced by QuerycatParser#query.
    def exitQuery(self, ctx: QuerycatParser.QueryContext):
        pass

    # Enter a parse tree produced by QuerycatParser#selectQuery.
    def enterSelectQuery(self, ctx: QuerycatParser.SelectQueryContext):
        pass

    # Exit a parse tree produced by QuerycatParser#selectQuery.
    def exitSelectQuery(self, ctx: QuerycatParser.SelectQueryContext):
        pass

    # Enter a parse tree produced by QuerycatParser#subSelect.
    def enterSubSelect(self, ctx: QuerycatParser.SubSelectContext):
        pass

    # Exit a parse tree produced by QuerycatParser#subSelect.
    def exitSubSelect(self, ctx: QuerycatParser.SubSelectContext):
        pass

    # Enter a parse tree produced by QuerycatParser#selectClause.
    def enterSelectClause(self, ctx: QuerycatParser.SelectClauseContext):
        pass

    # Exit a parse tree produced by QuerycatParser#selectClause.
    def exitSelectClause(self, ctx: QuerycatParser.SelectClauseContext):
        pass

    # Enter a parse tree produced by QuerycatParser#selectGraphPattern.
    def enterSelectGraphPattern(self, ctx: QuerycatParser.SelectGraphPatternContext):
        pass

    # Exit a parse tree produced by QuerycatParser#selectGraphPattern.
    def exitSelectGraphPattern(self, ctx: QuerycatParser.SelectGraphPatternContext):
        pass

    # Enter a parse tree produced by QuerycatParser#fromClause.
    def enterFromClause(self, ctx: QuerycatParser.FromClauseContext):
        pass

    # Exit a parse tree produced by QuerycatParser#fromClause.
    def exitFromClause(self, ctx: QuerycatParser.FromClauseContext):
        pass

    # Enter a parse tree produced by QuerycatParser#whereClause.
    def enterWhereClause(self, ctx: QuerycatParser.WhereClauseContext):
        pass

    # Exit a parse tree produced by QuerycatParser#whereClause.
    def exitWhereClause(self, ctx: QuerycatParser.WhereClauseContext):
        pass

    # Enter a parse tree produced by QuerycatParser#solutionModifier.
    def enterSolutionModifier(self, ctx: QuerycatParser.SolutionModifierContext):
        pass

    # Exit a parse tree produced by QuerycatParser#solutionModifier.
    def exitSolutionModifier(self, ctx: QuerycatParser.SolutionModifierContext):
        pass

    # Enter a parse tree produced by QuerycatParser#limitOffsetClauses.
    def enterLimitOffsetClauses(self, ctx: QuerycatParser.LimitOffsetClausesContext):
        pass

    # Exit a parse tree produced by QuerycatParser#limitOffsetClauses.
    def exitLimitOffsetClauses(self, ctx: QuerycatParser.LimitOffsetClausesContext):
        pass

    # Enter a parse tree produced by QuerycatParser#orderClause.
    def enterOrderClause(self, ctx: QuerycatParser.OrderClauseContext):
        pass

    # Exit a parse tree produced by QuerycatParser#orderClause.
    def exitOrderClause(self, ctx: QuerycatParser.OrderClauseContext):
        pass

    # Enter a parse tree produced by QuerycatParser#orderCondition.
    def enterOrderCondition(self, ctx: QuerycatParser.OrderConditionContext):
        pass

    # Exit a parse tree produced by QuerycatParser#orderCondition.
    def exitOrderCondition(self, ctx: QuerycatParser.OrderConditionContext):
        pass

    # Enter a parse tree produced by QuerycatParser#limitClause.
    def enterLimitClause(self, ctx: QuerycatParser.LimitClauseContext):
        pass

    # Exit a parse tree produced by QuerycatParser#limitClause.
    def exitLimitClause(self, ctx: QuerycatParser.LimitClauseContext):
        pass

    # Enter a parse tree produced by QuerycatParser#offsetClause.
    def enterOffsetClause(self, ctx: QuerycatParser.OffsetClauseContext):
        pass

    # Exit a parse tree produced by QuerycatParser#offsetClause.
    def exitOffsetClause(self, ctx: QuerycatParser.OffsetClauseContext):
        pass

    # Enter a parse tree produced by QuerycatParser#groupGraphPattern.
    def enterGroupGraphPattern(self, ctx: QuerycatParser.GroupGraphPatternContext):
        pass

    # Exit a parse tree produced by QuerycatParser#groupGraphPattern.
    def exitGroupGraphPattern(self, ctx: QuerycatParser.GroupGraphPatternContext):
        pass

    # Enter a parse tree produced by QuerycatParser#triplesBlock.
    def enterTriplesBlock(self, ctx: QuerycatParser.TriplesBlockContext):
        pass

    # Exit a parse tree produced by QuerycatParser#triplesBlock.
    def exitTriplesBlock(self, ctx: QuerycatParser.TriplesBlockContext):
        pass

    # Enter a parse tree produced by QuerycatParser#graphPatternNotTriples.
    def enterGraphPatternNotTriples(
        self, ctx: QuerycatParser.GraphPatternNotTriplesContext
    ):
        pass

    # Exit a parse tree produced by QuerycatParser#graphPatternNotTriples.
    def exitGraphPatternNotTriples(
        self, ctx: QuerycatParser.GraphPatternNotTriplesContext
    ):
        pass

    # Enter a parse tree produced by QuerycatParser#optionalGraphPattern.
    def enterOptionalGraphPattern(
        self, ctx: QuerycatParser.OptionalGraphPatternContext
    ):
        pass

    # Exit a parse tree produced by QuerycatParser#optionalGraphPattern.
    def exitOptionalGraphPattern(self, ctx: QuerycatParser.OptionalGraphPatternContext):
        pass

    # Enter a parse tree produced by QuerycatParser#groupOrUnionGraphPattern.
    def enterGroupOrUnionGraphPattern(
        self, ctx: QuerycatParser.GroupOrUnionGraphPatternContext
    ):
        pass

    # Exit a parse tree produced by QuerycatParser#groupOrUnionGraphPattern.
    def exitGroupOrUnionGraphPattern(
        self, ctx: QuerycatParser.GroupOrUnionGraphPatternContext
    ):
        pass

    # Enter a parse tree produced by QuerycatParser#inlineData.
    def enterInlineData(self, ctx: QuerycatParser.InlineDataContext):
        pass

    # Exit a parse tree produced by QuerycatParser#inlineData.
    def exitInlineData(self, ctx: QuerycatParser.InlineDataContext):
        pass

    # Enter a parse tree produced by QuerycatParser#dataBlock.
    def enterDataBlock(self, ctx: QuerycatParser.DataBlockContext):
        pass

    # Exit a parse tree produced by QuerycatParser#dataBlock.
    def exitDataBlock(self, ctx: QuerycatParser.DataBlockContext):
        pass

    # Enter a parse tree produced by QuerycatParser#dataBlockValue.
    def enterDataBlockValue(self, ctx: QuerycatParser.DataBlockValueContext):
        pass

    # Exit a parse tree produced by QuerycatParser#dataBlockValue.
    def exitDataBlockValue(self, ctx: QuerycatParser.DataBlockValueContext):
        pass

    # Enter a parse tree produced by QuerycatParser#filter_.
    def enterFilter_(self, ctx: QuerycatParser.Filter_Context):
        pass

    # Exit a parse tree produced by QuerycatParser#filter_.
    def exitFilter_(self, ctx: QuerycatParser.Filter_Context):
        pass

    # Enter a parse tree produced by QuerycatParser#constraint.
    def enterConstraint(self, ctx: QuerycatParser.ConstraintContext):
        pass

    # Exit a parse tree produced by QuerycatParser#constraint.
    def exitConstraint(self, ctx: QuerycatParser.ConstraintContext):
        pass

    # Enter a parse tree produced by QuerycatParser#selectTriples.
    def enterSelectTriples(self, ctx: QuerycatParser.SelectTriplesContext):
        pass

    # Exit a parse tree produced by QuerycatParser#selectTriples.
    def exitSelectTriples(self, ctx: QuerycatParser.SelectTriplesContext):
        pass

    # Enter a parse tree produced by QuerycatParser#triplesSameSubject.
    def enterTriplesSameSubject(self, ctx: QuerycatParser.TriplesSameSubjectContext):
        pass

    # Exit a parse tree produced by QuerycatParser#triplesSameSubject.
    def exitTriplesSameSubject(self, ctx: QuerycatParser.TriplesSameSubjectContext):
        pass

    # Enter a parse tree produced by QuerycatParser#propertyListNotEmpty.
    def enterPropertyListNotEmpty(
        self, ctx: QuerycatParser.PropertyListNotEmptyContext
    ):
        pass

    # Exit a parse tree produced by QuerycatParser#propertyListNotEmpty.
    def exitPropertyListNotEmpty(self, ctx: QuerycatParser.PropertyListNotEmptyContext):
        pass

    # Enter a parse tree produced by QuerycatParser#propertyList.
    def enterPropertyList(self, ctx: QuerycatParser.PropertyListContext):
        pass

    # Exit a parse tree produced by QuerycatParser#propertyList.
    def exitPropertyList(self, ctx: QuerycatParser.PropertyListContext):
        pass

    # Enter a parse tree produced by QuerycatParser#objectList.
    def enterObjectList(self, ctx: QuerycatParser.ObjectListContext):
        pass

    # Exit a parse tree produced by QuerycatParser#objectList.
    def exitObjectList(self, ctx: QuerycatParser.ObjectListContext):
        pass

    # Enter a parse tree produced by QuerycatParser#object_.
    def enterObject_(self, ctx: QuerycatParser.Object_Context):
        pass

    # Exit a parse tree produced by QuerycatParser#object_.
    def exitObject_(self, ctx: QuerycatParser.Object_Context):
        pass

    # Enter a parse tree produced by QuerycatParser#verb.
    def enterVerb(self, ctx: QuerycatParser.VerbContext):
        pass

    # Exit a parse tree produced by QuerycatParser#verb.
    def exitVerb(self, ctx: QuerycatParser.VerbContext):
        pass

    # Enter a parse tree produced by QuerycatParser#schemaMorphismOrPath.
    def enterSchemaMorphismOrPath(
        self, ctx: QuerycatParser.SchemaMorphismOrPathContext
    ):
        pass

    # Exit a parse tree produced by QuerycatParser#schemaMorphismOrPath.
    def exitSchemaMorphismOrPath(self, ctx: QuerycatParser.SchemaMorphismOrPathContext):
        pass

    # Enter a parse tree produced by QuerycatParser#pathAlternative.
    def enterPathAlternative(self, ctx: QuerycatParser.PathAlternativeContext):
        pass

    # Exit a parse tree produced by QuerycatParser#pathAlternative.
    def exitPathAlternative(self, ctx: QuerycatParser.PathAlternativeContext):
        pass

    # Enter a parse tree produced by QuerycatParser#pathSequence.
    def enterPathSequence(self, ctx: QuerycatParser.PathSequenceContext):
        pass

    # Exit a parse tree produced by QuerycatParser#pathSequence.
    def exitPathSequence(self, ctx: QuerycatParser.PathSequenceContext):
        pass

    # Enter a parse tree produced by QuerycatParser#pathWithMod.
    def enterPathWithMod(self, ctx: QuerycatParser.PathWithModContext):
        pass

    # Exit a parse tree produced by QuerycatParser#pathWithMod.
    def exitPathWithMod(self, ctx: QuerycatParser.PathWithModContext):
        pass

    # Enter a parse tree produced by QuerycatParser#pathMod.
    def enterPathMod(self, ctx: QuerycatParser.PathModContext):
        pass

    # Exit a parse tree produced by QuerycatParser#pathMod.
    def exitPathMod(self, ctx: QuerycatParser.PathModContext):
        pass

    # Enter a parse tree produced by QuerycatParser#pathPrimary.
    def enterPathPrimary(self, ctx: QuerycatParser.PathPrimaryContext):
        pass

    # Exit a parse tree produced by QuerycatParser#pathPrimary.
    def exitPathPrimary(self, ctx: QuerycatParser.PathPrimaryContext):
        pass

    # Enter a parse tree produced by QuerycatParser#schemaMorphism.
    def enterSchemaMorphism(self, ctx: QuerycatParser.SchemaMorphismContext):
        pass

    # Exit a parse tree produced by QuerycatParser#schemaMorphism.
    def exitSchemaMorphism(self, ctx: QuerycatParser.SchemaMorphismContext):
        pass

    # Enter a parse tree produced by QuerycatParser#primaryMorphism.
    def enterPrimaryMorphism(self, ctx: QuerycatParser.PrimaryMorphismContext):
        pass

    # Exit a parse tree produced by QuerycatParser#primaryMorphism.
    def exitPrimaryMorphism(self, ctx: QuerycatParser.PrimaryMorphismContext):
        pass

    # Enter a parse tree produced by QuerycatParser#dualMorphism.
    def enterDualMorphism(self, ctx: QuerycatParser.DualMorphismContext):
        pass

    # Exit a parse tree produced by QuerycatParser#dualMorphism.
    def exitDualMorphism(self, ctx: QuerycatParser.DualMorphismContext):
        pass

    # Enter a parse tree produced by QuerycatParser#graphNode.
    def enterGraphNode(self, ctx: QuerycatParser.GraphNodeContext):
        pass

    # Exit a parse tree produced by QuerycatParser#graphNode.
    def exitGraphNode(self, ctx: QuerycatParser.GraphNodeContext):
        pass

    # Enter a parse tree produced by QuerycatParser#varOrTerm.
    def enterVarOrTerm(self, ctx: QuerycatParser.VarOrTermContext):
        pass

    # Exit a parse tree produced by QuerycatParser#varOrTerm.
    def exitVarOrTerm(self, ctx: QuerycatParser.VarOrTermContext):
        pass

    # Enter a parse tree produced by QuerycatParser#var_.
    def enterVar_(self, ctx: QuerycatParser.Var_Context):
        pass

    # Exit a parse tree produced by QuerycatParser#var_.
    def exitVar_(self, ctx: QuerycatParser.Var_Context):
        pass

    # Enter a parse tree produced by QuerycatParser#constantTerm.
    def enterConstantTerm(self, ctx: QuerycatParser.ConstantTermContext):
        pass

    # Exit a parse tree produced by QuerycatParser#constantTerm.
    def exitConstantTerm(self, ctx: QuerycatParser.ConstantTermContext):
        pass

    # Enter a parse tree produced by QuerycatParser#aggregationTerm.
    def enterAggregationTerm(self, ctx: QuerycatParser.AggregationTermContext):
        pass

    # Exit a parse tree produced by QuerycatParser#aggregationTerm.
    def exitAggregationTerm(self, ctx: QuerycatParser.AggregationTermContext):
        pass

    # Enter a parse tree produced by QuerycatParser#distinctModifier.
    def enterDistinctModifier(self, ctx: QuerycatParser.DistinctModifierContext):
        pass

    # Exit a parse tree produced by QuerycatParser#distinctModifier.
    def exitDistinctModifier(self, ctx: QuerycatParser.DistinctModifierContext):
        pass

    # Enter a parse tree produced by QuerycatParser#aggregationFunc.
    def enterAggregationFunc(self, ctx: QuerycatParser.AggregationFuncContext):
        pass

    # Exit a parse tree produced by QuerycatParser#aggregationFunc.
    def exitAggregationFunc(self, ctx: QuerycatParser.AggregationFuncContext):
        pass

    # Enter a parse tree produced by QuerycatParser#expression.
    def enterExpression(self, ctx: QuerycatParser.ExpressionContext):
        pass

    # Exit a parse tree produced by QuerycatParser#expression.
    def exitExpression(self, ctx: QuerycatParser.ExpressionContext):
        pass

    # Enter a parse tree produced by QuerycatParser#conditionalOrExpression.
    def enterConditionalOrExpression(
        self, ctx: QuerycatParser.ConditionalOrExpressionContext
    ):
        pass

    # Exit a parse tree produced by QuerycatParser#conditionalOrExpression.
    def exitConditionalOrExpression(
        self, ctx: QuerycatParser.ConditionalOrExpressionContext
    ):
        pass

    # Enter a parse tree produced by QuerycatParser#conditionalAndExpression.
    def enterConditionalAndExpression(
        self, ctx: QuerycatParser.ConditionalAndExpressionContext
    ):
        pass

    # Exit a parse tree produced by QuerycatParser#conditionalAndExpression.
    def exitConditionalAndExpression(
        self, ctx: QuerycatParser.ConditionalAndExpressionContext
    ):
        pass

    # Enter a parse tree produced by QuerycatParser#valueLogical.
    def enterValueLogical(self, ctx: QuerycatParser.ValueLogicalContext):
        pass

    # Exit a parse tree produced by QuerycatParser#valueLogical.
    def exitValueLogical(self, ctx: QuerycatParser.ValueLogicalContext):
        pass

    # Enter a parse tree produced by QuerycatParser#relationalExpression.
    def enterRelationalExpression(
        self, ctx: QuerycatParser.RelationalExpressionContext
    ):
        pass

    # Exit a parse tree produced by QuerycatParser#relationalExpression.
    def exitRelationalExpression(self, ctx: QuerycatParser.RelationalExpressionContext):
        pass

    # Enter a parse tree produced by QuerycatParser#expressionPart.
    def enterExpressionPart(self, ctx: QuerycatParser.ExpressionPartContext):
        pass

    # Exit a parse tree produced by QuerycatParser#expressionPart.
    def exitExpressionPart(self, ctx: QuerycatParser.ExpressionPartContext):
        pass

    # Enter a parse tree produced by QuerycatParser#primaryExpression.
    def enterPrimaryExpression(self, ctx: QuerycatParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by QuerycatParser#primaryExpression.
    def exitPrimaryExpression(self, ctx: QuerycatParser.PrimaryExpressionContext):
        pass

    # Enter a parse tree produced by QuerycatParser#brackettedExpression.
    def enterBrackettedExpression(
        self, ctx: QuerycatParser.BrackettedExpressionContext
    ):
        pass

    # Exit a parse tree produced by QuerycatParser#brackettedExpression.
    def exitBrackettedExpression(self, ctx: QuerycatParser.BrackettedExpressionContext):
        pass

    # Enter a parse tree produced by QuerycatParser#numericLiteral.
    def enterNumericLiteral(self, ctx: QuerycatParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by QuerycatParser#numericLiteral.
    def exitNumericLiteral(self, ctx: QuerycatParser.NumericLiteralContext):
        pass

    # Enter a parse tree produced by QuerycatParser#numericLiteralUnsigned.
    def enterNumericLiteralUnsigned(
        self, ctx: QuerycatParser.NumericLiteralUnsignedContext
    ):
        pass

    # Exit a parse tree produced by QuerycatParser#numericLiteralUnsigned.
    def exitNumericLiteralUnsigned(
        self, ctx: QuerycatParser.NumericLiteralUnsignedContext
    ):
        pass

    # Enter a parse tree produced by QuerycatParser#numericLiteralPositive.
    def enterNumericLiteralPositive(
        self, ctx: QuerycatParser.NumericLiteralPositiveContext
    ):
        pass

    # Exit a parse tree produced by QuerycatParser#numericLiteralPositive.
    def exitNumericLiteralPositive(
        self, ctx: QuerycatParser.NumericLiteralPositiveContext
    ):
        pass

    # Enter a parse tree produced by QuerycatParser#numericLiteralNegative.
    def enterNumericLiteralNegative(
        self, ctx: QuerycatParser.NumericLiteralNegativeContext
    ):
        pass

    # Exit a parse tree produced by QuerycatParser#numericLiteralNegative.
    def exitNumericLiteralNegative(
        self, ctx: QuerycatParser.NumericLiteralNegativeContext
    ):
        pass

    # Enter a parse tree produced by QuerycatParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx: QuerycatParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by QuerycatParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx: QuerycatParser.BooleanLiteralContext):
        pass

    # Enter a parse tree produced by QuerycatParser#string_.
    def enterString_(self, ctx: QuerycatParser.String_Context):
        pass

    # Exit a parse tree produced by QuerycatParser#string_.
    def exitString_(self, ctx: QuerycatParser.String_Context):
        pass

    # Enter a parse tree produced by QuerycatParser#blankNode.
    def enterBlankNode(self, ctx: QuerycatParser.BlankNodeContext):
        pass

    # Exit a parse tree produced by QuerycatParser#blankNode.
    def exitBlankNode(self, ctx: QuerycatParser.BlankNodeContext):
        pass


del QuerycatParser
