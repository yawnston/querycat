# Generated from grammars/Querycat.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,63,360,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,1,0,1,0,1,0,1,1,1,1,
        1,1,1,1,1,2,1,2,1,2,1,3,1,3,3,3,115,8,3,1,3,1,3,1,4,3,4,120,8,4,
        1,4,1,4,1,5,3,5,125,8,5,1,5,3,5,128,8,5,1,6,1,6,3,6,132,8,6,1,6,
        1,6,3,6,136,8,6,3,6,138,8,6,1,7,1,7,1,7,4,7,143,8,7,11,7,12,7,144,
        1,8,1,8,1,8,1,8,3,8,151,8,8,3,8,153,8,8,1,9,1,9,1,9,1,10,1,10,1,
        10,1,11,1,11,3,11,163,8,11,1,11,1,11,3,11,167,8,11,1,11,3,11,170,
        8,11,1,11,3,11,173,8,11,5,11,175,8,11,10,11,12,11,178,9,11,1,11,
        1,11,1,12,1,12,1,12,3,12,185,8,12,3,12,187,8,12,1,13,1,13,3,13,191,
        8,13,1,14,1,14,1,14,1,15,1,15,1,15,5,15,199,8,15,10,15,12,15,202,
        9,15,1,16,1,16,1,16,1,17,1,17,1,18,1,18,1,18,3,18,212,8,18,3,18,
        214,8,18,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,3,20,225,8,
        20,5,20,227,8,20,10,20,12,20,230,9,20,1,21,3,21,233,8,21,1,22,1,
        22,1,22,5,22,238,8,22,10,22,12,22,241,9,22,1,23,1,23,1,24,1,24,1,
        25,1,25,1,25,5,25,250,8,25,10,25,12,25,253,9,25,1,26,1,26,3,26,257,
        8,26,1,27,1,27,1,28,1,28,1,28,1,29,1,29,1,29,3,29,267,8,29,1,30,
        1,30,1,30,3,30,272,8,30,1,31,1,31,1,32,1,32,1,32,1,32,1,32,3,32,
        281,8,32,1,33,1,33,1,33,3,33,286,8,33,1,33,1,33,1,33,1,34,1,34,1,
        35,1,35,1,36,1,36,1,37,1,37,1,37,5,37,300,8,37,10,37,12,37,303,9,
        37,1,38,1,38,1,38,5,38,308,8,38,10,38,12,38,311,9,38,1,39,1,39,1,
        40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,3,
        40,328,8,40,1,41,1,41,1,42,1,42,1,42,1,42,1,42,3,42,337,8,42,1,43,
        1,43,1,43,1,43,1,44,1,44,1,44,3,44,346,8,44,1,45,1,45,1,46,1,46,
        1,47,1,47,1,48,1,48,1,49,1,49,1,50,1,50,1,50,0,0,51,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,
        100,0,9,1,0,7,8,1,0,40,41,1,0,23,27,1,0,42,44,1,0,45,47,1,0,48,50,
        1,0,36,37,1,0,52,53,2,0,39,39,58,58,357,0,102,1,0,0,0,2,105,1,0,
        0,0,4,109,1,0,0,0,6,112,1,0,0,0,8,119,1,0,0,0,10,124,1,0,0,0,12,
        137,1,0,0,0,14,139,1,0,0,0,16,152,1,0,0,0,18,154,1,0,0,0,20,157,
        1,0,0,0,22,160,1,0,0,0,24,181,1,0,0,0,26,190,1,0,0,0,28,192,1,0,
        0,0,30,195,1,0,0,0,32,203,1,0,0,0,34,206,1,0,0,0,36,208,1,0,0,0,
        38,215,1,0,0,0,40,218,1,0,0,0,42,232,1,0,0,0,44,234,1,0,0,0,46,242,
        1,0,0,0,48,244,1,0,0,0,50,246,1,0,0,0,52,256,1,0,0,0,54,258,1,0,
        0,0,56,260,1,0,0,0,58,263,1,0,0,0,60,271,1,0,0,0,62,273,1,0,0,0,
        64,280,1,0,0,0,66,282,1,0,0,0,68,290,1,0,0,0,70,292,1,0,0,0,72,294,
        1,0,0,0,74,296,1,0,0,0,76,304,1,0,0,0,78,312,1,0,0,0,80,314,1,0,
        0,0,82,329,1,0,0,0,84,336,1,0,0,0,86,338,1,0,0,0,88,345,1,0,0,0,
        90,347,1,0,0,0,92,349,1,0,0,0,94,351,1,0,0,0,96,353,1,0,0,0,98,355,
        1,0,0,0,100,357,1,0,0,0,102,103,3,2,1,0,103,104,5,0,0,1,104,1,1,
        0,0,0,105,106,3,4,2,0,106,107,3,8,4,0,107,108,3,10,5,0,108,3,1,0,
        0,0,109,110,5,1,0,0,110,111,3,6,3,0,111,5,1,0,0,0,112,114,5,2,0,
        0,113,115,3,36,18,0,114,113,1,0,0,0,114,115,1,0,0,0,115,116,1,0,
        0,0,116,117,5,3,0,0,117,7,1,0,0,0,118,120,5,4,0,0,119,118,1,0,0,
        0,119,120,1,0,0,0,120,121,1,0,0,0,121,122,3,22,11,0,122,9,1,0,0,
        0,123,125,3,14,7,0,124,123,1,0,0,0,124,125,1,0,0,0,125,127,1,0,0,
        0,126,128,3,12,6,0,127,126,1,0,0,0,127,128,1,0,0,0,128,11,1,0,0,
        0,129,131,3,18,9,0,130,132,3,20,10,0,131,130,1,0,0,0,131,132,1,0,
        0,0,132,138,1,0,0,0,133,135,3,20,10,0,134,136,3,18,9,0,135,134,1,
        0,0,0,135,136,1,0,0,0,136,138,1,0,0,0,137,129,1,0,0,0,137,133,1,
        0,0,0,138,13,1,0,0,0,139,140,5,5,0,0,140,142,5,6,0,0,141,143,3,16,
        8,0,142,141,1,0,0,0,143,144,1,0,0,0,144,142,1,0,0,0,144,145,1,0,
        0,0,145,15,1,0,0,0,146,147,7,0,0,0,147,153,3,86,43,0,148,151,3,34,
        17,0,149,151,3,62,31,0,150,148,1,0,0,0,150,149,1,0,0,0,151,153,1,
        0,0,0,152,146,1,0,0,0,152,150,1,0,0,0,153,17,1,0,0,0,154,155,5,9,
        0,0,155,156,5,42,0,0,156,19,1,0,0,0,157,158,5,10,0,0,158,159,5,42,
        0,0,159,21,1,0,0,0,160,162,5,2,0,0,161,163,3,24,12,0,162,161,1,0,
        0,0,162,163,1,0,0,0,163,176,1,0,0,0,164,167,3,26,13,0,165,167,3,
        32,16,0,166,164,1,0,0,0,166,165,1,0,0,0,167,169,1,0,0,0,168,170,
        5,11,0,0,169,168,1,0,0,0,169,170,1,0,0,0,170,172,1,0,0,0,171,173,
        3,24,12,0,172,171,1,0,0,0,172,173,1,0,0,0,173,175,1,0,0,0,174,166,
        1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,179,
        1,0,0,0,178,176,1,0,0,0,179,180,5,3,0,0,180,23,1,0,0,0,181,186,3,
        38,19,0,182,184,5,11,0,0,183,185,3,24,12,0,184,183,1,0,0,0,184,185,
        1,0,0,0,185,187,1,0,0,0,186,182,1,0,0,0,186,187,1,0,0,0,187,25,1,
        0,0,0,188,191,3,28,14,0,189,191,3,30,15,0,190,188,1,0,0,0,190,189,
        1,0,0,0,191,27,1,0,0,0,192,193,5,12,0,0,193,194,3,22,11,0,194,29,
        1,0,0,0,195,200,3,22,11,0,196,197,5,13,0,0,197,199,3,22,11,0,198,
        196,1,0,0,0,199,202,1,0,0,0,200,198,1,0,0,0,200,201,1,0,0,0,201,
        31,1,0,0,0,202,200,1,0,0,0,203,204,5,14,0,0,204,205,3,34,17,0,205,
        33,1,0,0,0,206,207,3,86,43,0,207,35,1,0,0,0,208,213,3,38,19,0,209,
        211,5,11,0,0,210,212,3,36,18,0,211,210,1,0,0,0,211,212,1,0,0,0,212,
        214,1,0,0,0,213,209,1,0,0,0,213,214,1,0,0,0,214,37,1,0,0,0,215,216,
        3,60,30,0,216,217,3,40,20,0,217,39,1,0,0,0,218,219,3,48,24,0,219,
        228,3,44,22,0,220,224,5,15,0,0,221,222,3,48,24,0,222,223,3,44,22,
        0,223,225,1,0,0,0,224,221,1,0,0,0,224,225,1,0,0,0,225,227,1,0,0,
        0,226,220,1,0,0,0,227,230,1,0,0,0,228,226,1,0,0,0,228,229,1,0,0,
        0,229,41,1,0,0,0,230,228,1,0,0,0,231,233,3,40,20,0,232,231,1,0,0,
        0,232,233,1,0,0,0,233,43,1,0,0,0,234,239,3,46,23,0,235,236,5,16,
        0,0,236,238,3,46,23,0,237,235,1,0,0,0,238,241,1,0,0,0,239,237,1,
        0,0,0,239,240,1,0,0,0,240,45,1,0,0,0,241,239,1,0,0,0,242,243,3,58,
        29,0,243,47,1,0,0,0,244,245,3,50,25,0,245,49,1,0,0,0,246,251,3,52,
        26,0,247,248,5,17,0,0,248,250,3,52,26,0,249,247,1,0,0,0,250,253,
        1,0,0,0,251,249,1,0,0,0,251,252,1,0,0,0,252,51,1,0,0,0,253,251,1,
        0,0,0,254,257,3,54,27,0,255,257,3,56,28,0,256,254,1,0,0,0,256,255,
        1,0,0,0,257,53,1,0,0,0,258,259,5,38,0,0,259,55,1,0,0,0,260,261,5,
        18,0,0,261,262,3,54,27,0,262,57,1,0,0,0,263,266,3,60,30,0,264,265,
        5,19,0,0,265,267,3,62,31,0,266,264,1,0,0,0,266,267,1,0,0,0,267,59,
        1,0,0,0,268,272,3,62,31,0,269,272,3,64,32,0,270,272,3,66,33,0,271,
        268,1,0,0,0,271,269,1,0,0,0,271,270,1,0,0,0,272,61,1,0,0,0,273,274,
        7,1,0,0,274,63,1,0,0,0,275,281,3,88,44,0,276,281,3,96,48,0,277,281,
        3,98,49,0,278,281,3,100,50,0,279,281,5,57,0,0,280,275,1,0,0,0,280,
        276,1,0,0,0,280,277,1,0,0,0,280,278,1,0,0,0,280,279,1,0,0,0,281,
        65,1,0,0,0,282,283,3,70,35,0,283,285,5,20,0,0,284,286,3,68,34,0,
        285,284,1,0,0,0,285,286,1,0,0,0,286,287,1,0,0,0,287,288,3,62,31,
        0,288,289,5,21,0,0,289,67,1,0,0,0,290,291,5,22,0,0,291,69,1,0,0,
        0,292,293,7,2,0,0,293,71,1,0,0,0,294,295,3,74,37,0,295,73,1,0,0,
        0,296,301,3,76,38,0,297,298,5,28,0,0,298,300,3,76,38,0,299,297,1,
        0,0,0,300,303,1,0,0,0,301,299,1,0,0,0,301,302,1,0,0,0,302,75,1,0,
        0,0,303,301,1,0,0,0,304,309,3,78,39,0,305,306,5,29,0,0,306,308,3,
        78,39,0,307,305,1,0,0,0,308,311,1,0,0,0,309,307,1,0,0,0,309,310,
        1,0,0,0,310,77,1,0,0,0,311,309,1,0,0,0,312,313,3,80,40,0,313,79,
        1,0,0,0,314,327,3,82,41,0,315,316,5,30,0,0,316,328,3,82,41,0,317,
        318,5,31,0,0,318,328,3,82,41,0,319,320,5,32,0,0,320,328,3,82,41,
        0,321,322,5,33,0,0,322,328,3,82,41,0,323,324,5,34,0,0,324,328,3,
        82,41,0,325,326,5,35,0,0,326,328,3,82,41,0,327,315,1,0,0,0,327,317,
        1,0,0,0,327,319,1,0,0,0,327,321,1,0,0,0,327,323,1,0,0,0,327,325,
        1,0,0,0,327,328,1,0,0,0,328,81,1,0,0,0,329,330,3,84,42,0,330,83,
        1,0,0,0,331,337,3,86,43,0,332,337,3,88,44,0,333,337,3,96,48,0,334,
        337,3,98,49,0,335,337,3,62,31,0,336,331,1,0,0,0,336,332,1,0,0,0,
        336,333,1,0,0,0,336,334,1,0,0,0,336,335,1,0,0,0,337,85,1,0,0,0,338,
        339,5,20,0,0,339,340,3,72,36,0,340,341,5,21,0,0,341,87,1,0,0,0,342,
        346,3,90,45,0,343,346,3,92,46,0,344,346,3,94,47,0,345,342,1,0,0,
        0,345,343,1,0,0,0,345,344,1,0,0,0,346,89,1,0,0,0,347,348,7,3,0,0,
        348,91,1,0,0,0,349,350,7,4,0,0,350,93,1,0,0,0,351,352,7,5,0,0,352,
        95,1,0,0,0,353,354,7,6,0,0,354,97,1,0,0,0,355,356,7,7,0,0,356,99,
        1,0,0,0,357,358,7,8,0,0,358,101,1,0,0,0,36,114,119,124,127,131,135,
        137,144,150,152,162,166,169,172,176,184,186,190,200,211,213,224,
        228,232,239,251,256,266,271,280,285,301,309,327,336,345
    ]

class QuerycatParser ( Parser ):

    grammarFileName = "Querycat.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'SELECT'", "'{'", "'}'", "'WHERE'", "'ORDER'", 
                     "'BY'", "'ASC'", "'DESC'", "'LIMIT'", "'OFFSET'", "'.'", 
                     "'OPTIONAL'", "'UNION'", "'FILTER'", "';'", "','", 
                     "'/'", "'-'", "'AS'", "'('", "')'", "'DISTINCT'", "'COUNT'", 
                     "'SUM'", "'AVG'", "'MIN'", "'MAX'", "'||'", "'&&'", 
                     "'='", "'!='", "'<'", "'>'", "'<='", "'>='", "'true'", 
                     "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SCHEMA_MORPHISM", "BLANK_NODE_LABEL", 
                      "VAR1", "VAR2", "INTEGER", "DECIMAL", "DOUBLE", "INTEGER_POSITIVE", 
                      "DECIMAL_POSITIVE", "DOUBLE_POSITIVE", "INTEGER_NEGATIVE", 
                      "DECIMAL_NEGATIVE", "DOUBLE_NEGATIVE", "EXPONENT", 
                      "STRING_LITERAL1", "STRING_LITERAL2", "STRING_LITERAL_LONG1", 
                      "STRING_LITERAL_LONG2", "ECHAR", "NIL", "ANON", "PN_CHARS_U", 
                      "VARNAME", "PN_PREFIX", "PN_LOCAL", "WS" ]

    RULE_query = 0
    RULE_selectQuery = 1
    RULE_selectClause = 2
    RULE_selectGraphPattern = 3
    RULE_whereClause = 4
    RULE_solutionModifier = 5
    RULE_limitOffsetClauses = 6
    RULE_orderClause = 7
    RULE_orderCondition = 8
    RULE_limitClause = 9
    RULE_offsetClause = 10
    RULE_groupGraphPattern = 11
    RULE_triplesBlock = 12
    RULE_graphPatternNotTriples = 13
    RULE_optionalGraphPattern = 14
    RULE_groupOrUnionGraphPattern = 15
    RULE_filter_ = 16
    RULE_constraint = 17
    RULE_selectTriples = 18
    RULE_triplesSameSubject = 19
    RULE_propertyListNotEmpty = 20
    RULE_propertyList = 21
    RULE_objectList = 22
    RULE_object_ = 23
    RULE_verb = 24
    RULE_schemaMorphismOrPath = 25
    RULE_schemaMorphism = 26
    RULE_primaryMorphism = 27
    RULE_dualMorphism = 28
    RULE_graphNode = 29
    RULE_varOrTerm = 30
    RULE_var_ = 31
    RULE_constantTerm = 32
    RULE_aggregationTerm = 33
    RULE_distinctModifier = 34
    RULE_aggregationFunc = 35
    RULE_expression = 36
    RULE_conditionalOrExpression = 37
    RULE_conditionalAndExpression = 38
    RULE_valueLogical = 39
    RULE_relationalExpression = 40
    RULE_expressionPart = 41
    RULE_primaryExpression = 42
    RULE_brackettedExpression = 43
    RULE_numericLiteral = 44
    RULE_numericLiteralUnsigned = 45
    RULE_numericLiteralPositive = 46
    RULE_numericLiteralNegative = 47
    RULE_booleanLiteral = 48
    RULE_string_ = 49
    RULE_blankNode = 50

    ruleNames =  [ "query", "selectQuery", "selectClause", "selectGraphPattern", 
                   "whereClause", "solutionModifier", "limitOffsetClauses", 
                   "orderClause", "orderCondition", "limitClause", "offsetClause", 
                   "groupGraphPattern", "triplesBlock", "graphPatternNotTriples", 
                   "optionalGraphPattern", "groupOrUnionGraphPattern", "filter_", 
                   "constraint", "selectTriples", "triplesSameSubject", 
                   "propertyListNotEmpty", "propertyList", "objectList", 
                   "object_", "verb", "schemaMorphismOrPath", "schemaMorphism", 
                   "primaryMorphism", "dualMorphism", "graphNode", "varOrTerm", 
                   "var_", "constantTerm", "aggregationTerm", "distinctModifier", 
                   "aggregationFunc", "expression", "conditionalOrExpression", 
                   "conditionalAndExpression", "valueLogical", "relationalExpression", 
                   "expressionPart", "primaryExpression", "brackettedExpression", 
                   "numericLiteral", "numericLiteralUnsigned", "numericLiteralPositive", 
                   "numericLiteralNegative", "booleanLiteral", "string_", 
                   "blankNode" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    SCHEMA_MORPHISM=38
    BLANK_NODE_LABEL=39
    VAR1=40
    VAR2=41
    INTEGER=42
    DECIMAL=43
    DOUBLE=44
    INTEGER_POSITIVE=45
    DECIMAL_POSITIVE=46
    DOUBLE_POSITIVE=47
    INTEGER_NEGATIVE=48
    DECIMAL_NEGATIVE=49
    DOUBLE_NEGATIVE=50
    EXPONENT=51
    STRING_LITERAL1=52
    STRING_LITERAL2=53
    STRING_LITERAL_LONG1=54
    STRING_LITERAL_LONG2=55
    ECHAR=56
    NIL=57
    ANON=58
    PN_CHARS_U=59
    VARNAME=60
    PN_PREFIX=61
    PN_LOCAL=62
    WS=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def selectQuery(self):
            return self.getTypedRuleContext(QuerycatParser.SelectQueryContext,0)


        def EOF(self):
            return self.getToken(QuerycatParser.EOF, 0)

        def getRuleIndex(self):
            return QuerycatParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = QuerycatParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.selectQuery()
            self.state = 103
            self.match(QuerycatParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def selectClause(self):
            return self.getTypedRuleContext(QuerycatParser.SelectClauseContext,0)


        def whereClause(self):
            return self.getTypedRuleContext(QuerycatParser.WhereClauseContext,0)


        def solutionModifier(self):
            return self.getTypedRuleContext(QuerycatParser.SolutionModifierContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_selectQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectQuery" ):
                listener.enterSelectQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectQuery" ):
                listener.exitSelectQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectQuery" ):
                return visitor.visitSelectQuery(self)
            else:
                return visitor.visitChildren(self)




    def selectQuery(self):

        localctx = QuerycatParser.SelectQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_selectQuery)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.selectClause()
            self.state = 106
            self.whereClause()
            self.state = 107
            self.solutionModifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def selectGraphPattern(self):
            return self.getTypedRuleContext(QuerycatParser.SelectGraphPatternContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_selectClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectClause" ):
                listener.enterSelectClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectClause" ):
                listener.exitSelectClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectClause" ):
                return visitor.visitSelectClause(self)
            else:
                return visitor.visitChildren(self)




    def selectClause(self):

        localctx = QuerycatParser.SelectClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_selectClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(QuerycatParser.T__0)
            self.state = 110
            self.selectGraphPattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectGraphPatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def selectTriples(self):
            return self.getTypedRuleContext(QuerycatParser.SelectTriplesContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_selectGraphPattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectGraphPattern" ):
                listener.enterSelectGraphPattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectGraphPattern" ):
                listener.exitSelectGraphPattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectGraphPattern" ):
                return visitor.visitSelectGraphPattern(self)
            else:
                return visitor.visitChildren(self)




    def selectGraphPattern(self):

        localctx = QuerycatParser.SelectGraphPatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_selectGraphPattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(QuerycatParser.T__1)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 448107819586027520) != 0:
                self.state = 113
                self.selectTriples()


            self.state = 116
            self.match(QuerycatParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhereClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def groupGraphPattern(self):
            return self.getTypedRuleContext(QuerycatParser.GroupGraphPatternContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_whereClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhereClause" ):
                listener.enterWhereClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhereClause" ):
                listener.exitWhereClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhereClause" ):
                return visitor.visitWhereClause(self)
            else:
                return visitor.visitChildren(self)




    def whereClause(self):

        localctx = QuerycatParser.WhereClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_whereClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 118
                self.match(QuerycatParser.T__3)


            self.state = 121
            self.groupGraphPattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SolutionModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def orderClause(self):
            return self.getTypedRuleContext(QuerycatParser.OrderClauseContext,0)


        def limitOffsetClauses(self):
            return self.getTypedRuleContext(QuerycatParser.LimitOffsetClausesContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_solutionModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSolutionModifier" ):
                listener.enterSolutionModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSolutionModifier" ):
                listener.exitSolutionModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSolutionModifier" ):
                return visitor.visitSolutionModifier(self)
            else:
                return visitor.visitChildren(self)




    def solutionModifier(self):

        localctx = QuerycatParser.SolutionModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_solutionModifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 123
                self.orderClause()


            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9 or _la==10:
                self.state = 126
                self.limitOffsetClauses()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LimitOffsetClausesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def limitClause(self):
            return self.getTypedRuleContext(QuerycatParser.LimitClauseContext,0)


        def offsetClause(self):
            return self.getTypedRuleContext(QuerycatParser.OffsetClauseContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_limitOffsetClauses

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimitOffsetClauses" ):
                listener.enterLimitOffsetClauses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimitOffsetClauses" ):
                listener.exitLimitOffsetClauses(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLimitOffsetClauses" ):
                return visitor.visitLimitOffsetClauses(self)
            else:
                return visitor.visitChildren(self)




    def limitOffsetClauses(self):

        localctx = QuerycatParser.LimitOffsetClausesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_limitOffsetClauses)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.state = 129
                self.limitClause()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 130
                    self.offsetClause()


                pass
            elif token in [10]:
                self.state = 133
                self.offsetClause()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 134
                    self.limitClause()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def orderCondition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuerycatParser.OrderConditionContext)
            else:
                return self.getTypedRuleContext(QuerycatParser.OrderConditionContext,i)


        def getRuleIndex(self):
            return QuerycatParser.RULE_orderClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderClause" ):
                listener.enterOrderClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderClause" ):
                listener.exitOrderClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderClause" ):
                return visitor.visitOrderClause(self)
            else:
                return visitor.visitChildren(self)




    def orderClause(self):

        localctx = QuerycatParser.OrderClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_orderClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(QuerycatParser.T__4)
            self.state = 140
            self.match(QuerycatParser.T__5)
            self.state = 142 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 141
                self.orderCondition()
                self.state = 144 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 3298535932288) != 0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def brackettedExpression(self):
            return self.getTypedRuleContext(QuerycatParser.BrackettedExpressionContext,0)


        def constraint(self):
            return self.getTypedRuleContext(QuerycatParser.ConstraintContext,0)


        def var_(self):
            return self.getTypedRuleContext(QuerycatParser.Var_Context,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_orderCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderCondition" ):
                listener.enterOrderCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderCondition" ):
                listener.exitOrderCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderCondition" ):
                return visitor.visitOrderCondition(self)
            else:
                return visitor.visitChildren(self)




    def orderCondition(self):

        localctx = QuerycatParser.OrderConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_orderCondition)
        self._la = 0 # Token type
        try:
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 147
                self.brackettedExpression()
                pass
            elif token in [20, 40, 41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [20]:
                    self.state = 148
                    self.constraint()
                    pass
                elif token in [40, 41]:
                    self.state = 149
                    self.var_()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LimitClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(QuerycatParser.INTEGER, 0)

        def getRuleIndex(self):
            return QuerycatParser.RULE_limitClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimitClause" ):
                listener.enterLimitClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimitClause" ):
                listener.exitLimitClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLimitClause" ):
                return visitor.visitLimitClause(self)
            else:
                return visitor.visitChildren(self)




    def limitClause(self):

        localctx = QuerycatParser.LimitClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_limitClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(QuerycatParser.T__8)
            self.state = 155
            self.match(QuerycatParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OffsetClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(QuerycatParser.INTEGER, 0)

        def getRuleIndex(self):
            return QuerycatParser.RULE_offsetClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOffsetClause" ):
                listener.enterOffsetClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOffsetClause" ):
                listener.exitOffsetClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOffsetClause" ):
                return visitor.visitOffsetClause(self)
            else:
                return visitor.visitChildren(self)




    def offsetClause(self):

        localctx = QuerycatParser.OffsetClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_offsetClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(QuerycatParser.T__9)
            self.state = 158
            self.match(QuerycatParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroupGraphPatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def triplesBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuerycatParser.TriplesBlockContext)
            else:
                return self.getTypedRuleContext(QuerycatParser.TriplesBlockContext,i)


        def graphPatternNotTriples(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuerycatParser.GraphPatternNotTriplesContext)
            else:
                return self.getTypedRuleContext(QuerycatParser.GraphPatternNotTriplesContext,i)


        def filter_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuerycatParser.Filter_Context)
            else:
                return self.getTypedRuleContext(QuerycatParser.Filter_Context,i)


        def getRuleIndex(self):
            return QuerycatParser.RULE_groupGraphPattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroupGraphPattern" ):
                listener.enterGroupGraphPattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroupGraphPattern" ):
                listener.exitGroupGraphPattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroupGraphPattern" ):
                return visitor.visitGroupGraphPattern(self)
            else:
                return visitor.visitChildren(self)




    def groupGraphPattern(self):

        localctx = QuerycatParser.GroupGraphPatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_groupGraphPattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(QuerycatParser.T__1)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 448107819586027520) != 0:
                self.state = 161
                self.triplesBlock()


            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 20484) != 0:
                self.state = 166
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2, 12]:
                    self.state = 164
                    self.graphPatternNotTriples()
                    pass
                elif token in [14]:
                    self.state = 165
                    self.filter_()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 168
                    self.match(QuerycatParser.T__10)


                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 448107819586027520) != 0:
                    self.state = 171
                    self.triplesBlock()


                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 179
            self.match(QuerycatParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TriplesBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def triplesSameSubject(self):
            return self.getTypedRuleContext(QuerycatParser.TriplesSameSubjectContext,0)


        def triplesBlock(self):
            return self.getTypedRuleContext(QuerycatParser.TriplesBlockContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_triplesBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTriplesBlock" ):
                listener.enterTriplesBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTriplesBlock" ):
                listener.exitTriplesBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTriplesBlock" ):
                return visitor.visitTriplesBlock(self)
            else:
                return visitor.visitChildren(self)




    def triplesBlock(self):

        localctx = QuerycatParser.TriplesBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_triplesBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.triplesSameSubject()
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 182
                self.match(QuerycatParser.T__10)
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 448107819586027520) != 0:
                    self.state = 183
                    self.triplesBlock()




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GraphPatternNotTriplesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def optionalGraphPattern(self):
            return self.getTypedRuleContext(QuerycatParser.OptionalGraphPatternContext,0)


        def groupOrUnionGraphPattern(self):
            return self.getTypedRuleContext(QuerycatParser.GroupOrUnionGraphPatternContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_graphPatternNotTriples

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraphPatternNotTriples" ):
                listener.enterGraphPatternNotTriples(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraphPatternNotTriples" ):
                listener.exitGraphPatternNotTriples(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGraphPatternNotTriples" ):
                return visitor.visitGraphPatternNotTriples(self)
            else:
                return visitor.visitChildren(self)




    def graphPatternNotTriples(self):

        localctx = QuerycatParser.GraphPatternNotTriplesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_graphPatternNotTriples)
        try:
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.optionalGraphPattern()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.groupOrUnionGraphPattern()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionalGraphPatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def groupGraphPattern(self):
            return self.getTypedRuleContext(QuerycatParser.GroupGraphPatternContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_optionalGraphPattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptionalGraphPattern" ):
                listener.enterOptionalGraphPattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptionalGraphPattern" ):
                listener.exitOptionalGraphPattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptionalGraphPattern" ):
                return visitor.visitOptionalGraphPattern(self)
            else:
                return visitor.visitChildren(self)




    def optionalGraphPattern(self):

        localctx = QuerycatParser.OptionalGraphPatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_optionalGraphPattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(QuerycatParser.T__11)
            self.state = 193
            self.groupGraphPattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroupOrUnionGraphPatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def groupGraphPattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuerycatParser.GroupGraphPatternContext)
            else:
                return self.getTypedRuleContext(QuerycatParser.GroupGraphPatternContext,i)


        def getRuleIndex(self):
            return QuerycatParser.RULE_groupOrUnionGraphPattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroupOrUnionGraphPattern" ):
                listener.enterGroupOrUnionGraphPattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroupOrUnionGraphPattern" ):
                listener.exitGroupOrUnionGraphPattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroupOrUnionGraphPattern" ):
                return visitor.visitGroupOrUnionGraphPattern(self)
            else:
                return visitor.visitChildren(self)




    def groupOrUnionGraphPattern(self):

        localctx = QuerycatParser.GroupOrUnionGraphPatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_groupOrUnionGraphPattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.groupGraphPattern()
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 196
                self.match(QuerycatParser.T__12)
                self.state = 197
                self.groupGraphPattern()
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Filter_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constraint(self):
            return self.getTypedRuleContext(QuerycatParser.ConstraintContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_filter_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilter_" ):
                listener.enterFilter_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilter_" ):
                listener.exitFilter_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilter_" ):
                return visitor.visitFilter_(self)
            else:
                return visitor.visitChildren(self)




    def filter_(self):

        localctx = QuerycatParser.Filter_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_filter_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(QuerycatParser.T__13)
            self.state = 204
            self.constraint()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def brackettedExpression(self):
            return self.getTypedRuleContext(QuerycatParser.BrackettedExpressionContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstraint" ):
                listener.enterConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstraint" ):
                listener.exitConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstraint" ):
                return visitor.visitConstraint(self)
            else:
                return visitor.visitChildren(self)




    def constraint(self):

        localctx = QuerycatParser.ConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_constraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.brackettedExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectTriplesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def triplesSameSubject(self):
            return self.getTypedRuleContext(QuerycatParser.TriplesSameSubjectContext,0)


        def selectTriples(self):
            return self.getTypedRuleContext(QuerycatParser.SelectTriplesContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_selectTriples

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectTriples" ):
                listener.enterSelectTriples(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectTriples" ):
                listener.exitSelectTriples(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectTriples" ):
                return visitor.visitSelectTriples(self)
            else:
                return visitor.visitChildren(self)




    def selectTriples(self):

        localctx = QuerycatParser.SelectTriplesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_selectTriples)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.triplesSameSubject()
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 209
                self.match(QuerycatParser.T__10)
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 448107819586027520) != 0:
                    self.state = 210
                    self.selectTriples()




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TriplesSameSubjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varOrTerm(self):
            return self.getTypedRuleContext(QuerycatParser.VarOrTermContext,0)


        def propertyListNotEmpty(self):
            return self.getTypedRuleContext(QuerycatParser.PropertyListNotEmptyContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_triplesSameSubject

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTriplesSameSubject" ):
                listener.enterTriplesSameSubject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTriplesSameSubject" ):
                listener.exitTriplesSameSubject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTriplesSameSubject" ):
                return visitor.visitTriplesSameSubject(self)
            else:
                return visitor.visitChildren(self)




    def triplesSameSubject(self):

        localctx = QuerycatParser.TriplesSameSubjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_triplesSameSubject)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.varOrTerm()
            self.state = 216
            self.propertyListNotEmpty()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropertyListNotEmptyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def verb(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuerycatParser.VerbContext)
            else:
                return self.getTypedRuleContext(QuerycatParser.VerbContext,i)


        def objectList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuerycatParser.ObjectListContext)
            else:
                return self.getTypedRuleContext(QuerycatParser.ObjectListContext,i)


        def getRuleIndex(self):
            return QuerycatParser.RULE_propertyListNotEmpty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropertyListNotEmpty" ):
                listener.enterPropertyListNotEmpty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropertyListNotEmpty" ):
                listener.exitPropertyListNotEmpty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPropertyListNotEmpty" ):
                return visitor.visitPropertyListNotEmpty(self)
            else:
                return visitor.visitChildren(self)




    def propertyListNotEmpty(self):

        localctx = QuerycatParser.PropertyListNotEmptyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_propertyListNotEmpty)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.verb()
            self.state = 219
            self.objectList()
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 220
                self.match(QuerycatParser.T__14)
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==18 or _la==38:
                    self.state = 221
                    self.verb()
                    self.state = 222
                    self.objectList()


                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropertyListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def propertyListNotEmpty(self):
            return self.getTypedRuleContext(QuerycatParser.PropertyListNotEmptyContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_propertyList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropertyList" ):
                listener.enterPropertyList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropertyList" ):
                listener.exitPropertyList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPropertyList" ):
                return visitor.visitPropertyList(self)
            else:
                return visitor.visitChildren(self)




    def propertyList(self):

        localctx = QuerycatParser.PropertyListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_propertyList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18 or _la==38:
                self.state = 231
                self.propertyListNotEmpty()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def object_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuerycatParser.Object_Context)
            else:
                return self.getTypedRuleContext(QuerycatParser.Object_Context,i)


        def getRuleIndex(self):
            return QuerycatParser.RULE_objectList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectList" ):
                listener.enterObjectList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectList" ):
                listener.exitObjectList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjectList" ):
                return visitor.visitObjectList(self)
            else:
                return visitor.visitChildren(self)




    def objectList(self):

        localctx = QuerycatParser.ObjectListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_objectList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.object_()
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 235
                self.match(QuerycatParser.T__15)
                self.state = 236
                self.object_()
                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def graphNode(self):
            return self.getTypedRuleContext(QuerycatParser.GraphNodeContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_object_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_" ):
                listener.enterObject_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_" ):
                listener.exitObject_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_" ):
                return visitor.visitObject_(self)
            else:
                return visitor.visitChildren(self)




    def object_(self):

        localctx = QuerycatParser.Object_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_object_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.graphNode()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VerbContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def schemaMorphismOrPath(self):
            return self.getTypedRuleContext(QuerycatParser.SchemaMorphismOrPathContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_verb

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVerb" ):
                listener.enterVerb(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVerb" ):
                listener.exitVerb(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVerb" ):
                return visitor.visitVerb(self)
            else:
                return visitor.visitChildren(self)




    def verb(self):

        localctx = QuerycatParser.VerbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_verb)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.schemaMorphismOrPath()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SchemaMorphismOrPathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def schemaMorphism(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuerycatParser.SchemaMorphismContext)
            else:
                return self.getTypedRuleContext(QuerycatParser.SchemaMorphismContext,i)


        def getRuleIndex(self):
            return QuerycatParser.RULE_schemaMorphismOrPath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSchemaMorphismOrPath" ):
                listener.enterSchemaMorphismOrPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSchemaMorphismOrPath" ):
                listener.exitSchemaMorphismOrPath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSchemaMorphismOrPath" ):
                return visitor.visitSchemaMorphismOrPath(self)
            else:
                return visitor.visitChildren(self)




    def schemaMorphismOrPath(self):

        localctx = QuerycatParser.SchemaMorphismOrPathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_schemaMorphismOrPath)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.schemaMorphism()
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 247
                self.match(QuerycatParser.T__16)
                self.state = 248
                self.schemaMorphism()
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SchemaMorphismContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryMorphism(self):
            return self.getTypedRuleContext(QuerycatParser.PrimaryMorphismContext,0)


        def dualMorphism(self):
            return self.getTypedRuleContext(QuerycatParser.DualMorphismContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_schemaMorphism

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSchemaMorphism" ):
                listener.enterSchemaMorphism(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSchemaMorphism" ):
                listener.exitSchemaMorphism(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSchemaMorphism" ):
                return visitor.visitSchemaMorphism(self)
            else:
                return visitor.visitChildren(self)




    def schemaMorphism(self):

        localctx = QuerycatParser.SchemaMorphismContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_schemaMorphism)
        try:
            self.state = 256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.primaryMorphism()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.dualMorphism()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryMorphismContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCHEMA_MORPHISM(self):
            return self.getToken(QuerycatParser.SCHEMA_MORPHISM, 0)

        def getRuleIndex(self):
            return QuerycatParser.RULE_primaryMorphism

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryMorphism" ):
                listener.enterPrimaryMorphism(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryMorphism" ):
                listener.exitPrimaryMorphism(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryMorphism" ):
                return visitor.visitPrimaryMorphism(self)
            else:
                return visitor.visitChildren(self)




    def primaryMorphism(self):

        localctx = QuerycatParser.PrimaryMorphismContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_primaryMorphism)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(QuerycatParser.SCHEMA_MORPHISM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DualMorphismContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryMorphism(self):
            return self.getTypedRuleContext(QuerycatParser.PrimaryMorphismContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_dualMorphism

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDualMorphism" ):
                listener.enterDualMorphism(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDualMorphism" ):
                listener.exitDualMorphism(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDualMorphism" ):
                return visitor.visitDualMorphism(self)
            else:
                return visitor.visitChildren(self)




    def dualMorphism(self):

        localctx = QuerycatParser.DualMorphismContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_dualMorphism)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(QuerycatParser.T__17)
            self.state = 261
            self.primaryMorphism()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GraphNodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varOrTerm(self):
            return self.getTypedRuleContext(QuerycatParser.VarOrTermContext,0)


        def var_(self):
            return self.getTypedRuleContext(QuerycatParser.Var_Context,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_graphNode

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraphNode" ):
                listener.enterGraphNode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraphNode" ):
                listener.exitGraphNode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGraphNode" ):
                return visitor.visitGraphNode(self)
            else:
                return visitor.visitChildren(self)




    def graphNode(self):

        localctx = QuerycatParser.GraphNodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_graphNode)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.varOrTerm()
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 264
                self.match(QuerycatParser.T__18)
                self.state = 265
                self.var_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarOrTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_(self):
            return self.getTypedRuleContext(QuerycatParser.Var_Context,0)


        def constantTerm(self):
            return self.getTypedRuleContext(QuerycatParser.ConstantTermContext,0)


        def aggregationTerm(self):
            return self.getTypedRuleContext(QuerycatParser.AggregationTermContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_varOrTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarOrTerm" ):
                listener.enterVarOrTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarOrTerm" ):
                listener.exitVarOrTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarOrTerm" ):
                return visitor.visitVarOrTerm(self)
            else:
                return visitor.visitChildren(self)




    def varOrTerm(self):

        localctx = QuerycatParser.VarOrTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_varOrTerm)
        try:
            self.state = 271
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40, 41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.var_()
                pass
            elif token in [36, 37, 39, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 57, 58]:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.constantTerm()
                pass
            elif token in [23, 24, 25, 26, 27]:
                self.enterOuterAlt(localctx, 3)
                self.state = 270
                self.aggregationTerm()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR1(self):
            return self.getToken(QuerycatParser.VAR1, 0)

        def VAR2(self):
            return self.getToken(QuerycatParser.VAR2, 0)

        def getRuleIndex(self):
            return QuerycatParser.RULE_var_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_" ):
                listener.enterVar_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_" ):
                listener.exitVar_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_" ):
                return visitor.visitVar_(self)
            else:
                return visitor.visitChildren(self)




    def var_(self):

        localctx = QuerycatParser.Var_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_var_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            _la = self._input.LA(1)
            if not(_la==40 or _la==41):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numericLiteral(self):
            return self.getTypedRuleContext(QuerycatParser.NumericLiteralContext,0)


        def booleanLiteral(self):
            return self.getTypedRuleContext(QuerycatParser.BooleanLiteralContext,0)


        def string_(self):
            return self.getTypedRuleContext(QuerycatParser.String_Context,0)


        def blankNode(self):
            return self.getTypedRuleContext(QuerycatParser.BlankNodeContext,0)


        def NIL(self):
            return self.getToken(QuerycatParser.NIL, 0)

        def getRuleIndex(self):
            return QuerycatParser.RULE_constantTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantTerm" ):
                listener.enterConstantTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantTerm" ):
                listener.exitConstantTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstantTerm" ):
                return visitor.visitConstantTerm(self)
            else:
                return visitor.visitChildren(self)




    def constantTerm(self):

        localctx = QuerycatParser.ConstantTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_constantTerm)
        try:
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42, 43, 44, 45, 46, 47, 48, 49, 50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.numericLiteral()
                pass
            elif token in [36, 37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.booleanLiteral()
                pass
            elif token in [52, 53]:
                self.enterOuterAlt(localctx, 3)
                self.state = 277
                self.string_()
                pass
            elif token in [39, 58]:
                self.enterOuterAlt(localctx, 4)
                self.state = 278
                self.blankNode()
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 5)
                self.state = 279
                self.match(QuerycatParser.NIL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregationTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aggregationFunc(self):
            return self.getTypedRuleContext(QuerycatParser.AggregationFuncContext,0)


        def var_(self):
            return self.getTypedRuleContext(QuerycatParser.Var_Context,0)


        def distinctModifier(self):
            return self.getTypedRuleContext(QuerycatParser.DistinctModifierContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_aggregationTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregationTerm" ):
                listener.enterAggregationTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregationTerm" ):
                listener.exitAggregationTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregationTerm" ):
                return visitor.visitAggregationTerm(self)
            else:
                return visitor.visitChildren(self)




    def aggregationTerm(self):

        localctx = QuerycatParser.AggregationTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_aggregationTerm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.aggregationFunc()
            self.state = 283
            self.match(QuerycatParser.T__19)
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 284
                self.distinctModifier()


            self.state = 287
            self.var_()
            self.state = 288
            self.match(QuerycatParser.T__20)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DistinctModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QuerycatParser.RULE_distinctModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistinctModifier" ):
                listener.enterDistinctModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistinctModifier" ):
                listener.exitDistinctModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDistinctModifier" ):
                return visitor.visitDistinctModifier(self)
            else:
                return visitor.visitChildren(self)




    def distinctModifier(self):

        localctx = QuerycatParser.DistinctModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_distinctModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(QuerycatParser.T__21)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregationFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QuerycatParser.RULE_aggregationFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregationFunc" ):
                listener.enterAggregationFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregationFunc" ):
                listener.exitAggregationFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregationFunc" ):
                return visitor.visitAggregationFunc(self)
            else:
                return visitor.visitChildren(self)




    def aggregationFunc(self):

        localctx = QuerycatParser.AggregationFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_aggregationFunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 260046848) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionalOrExpression(self):
            return self.getTypedRuleContext(QuerycatParser.ConditionalOrExpressionContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = QuerycatParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.conditionalOrExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionalAndExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuerycatParser.ConditionalAndExpressionContext)
            else:
                return self.getTypedRuleContext(QuerycatParser.ConditionalAndExpressionContext,i)


        def getRuleIndex(self):
            return QuerycatParser.RULE_conditionalOrExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalOrExpression" ):
                listener.enterConditionalOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalOrExpression" ):
                listener.exitConditionalOrExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionalOrExpression" ):
                return visitor.visitConditionalOrExpression(self)
            else:
                return visitor.visitChildren(self)




    def conditionalOrExpression(self):

        localctx = QuerycatParser.ConditionalOrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_conditionalOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.conditionalAndExpression()
            self.state = 301
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 297
                self.match(QuerycatParser.T__27)
                self.state = 298
                self.conditionalAndExpression()
                self.state = 303
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalAndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def valueLogical(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuerycatParser.ValueLogicalContext)
            else:
                return self.getTypedRuleContext(QuerycatParser.ValueLogicalContext,i)


        def getRuleIndex(self):
            return QuerycatParser.RULE_conditionalAndExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalAndExpression" ):
                listener.enterConditionalAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalAndExpression" ):
                listener.exitConditionalAndExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionalAndExpression" ):
                return visitor.visitConditionalAndExpression(self)
            else:
                return visitor.visitChildren(self)




    def conditionalAndExpression(self):

        localctx = QuerycatParser.ConditionalAndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_conditionalAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.valueLogical()
            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 305
                self.match(QuerycatParser.T__28)
                self.state = 306
                self.valueLogical()
                self.state = 311
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueLogicalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self):
            return self.getTypedRuleContext(QuerycatParser.RelationalExpressionContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_valueLogical

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValueLogical" ):
                listener.enterValueLogical(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValueLogical" ):
                listener.exitValueLogical(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValueLogical" ):
                return visitor.visitValueLogical(self)
            else:
                return visitor.visitChildren(self)




    def valueLogical(self):

        localctx = QuerycatParser.ValueLogicalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_valueLogical)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.relationalExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionPart(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuerycatParser.ExpressionPartContext)
            else:
                return self.getTypedRuleContext(QuerycatParser.ExpressionPartContext,i)


        def getRuleIndex(self):
            return QuerycatParser.RULE_relationalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpression" ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpression" ):
                listener.exitRelationalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpression" ):
                return visitor.visitRelationalExpression(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpression(self):

        localctx = QuerycatParser.RelationalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_relationalExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.expressionPart()
            self.state = 327
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.state = 315
                self.match(QuerycatParser.T__29)
                self.state = 316
                self.expressionPart()
                pass
            elif token in [31]:
                self.state = 317
                self.match(QuerycatParser.T__30)
                self.state = 318
                self.expressionPart()
                pass
            elif token in [32]:
                self.state = 319
                self.match(QuerycatParser.T__31)
                self.state = 320
                self.expressionPart()
                pass
            elif token in [33]:
                self.state = 321
                self.match(QuerycatParser.T__32)
                self.state = 322
                self.expressionPart()
                pass
            elif token in [34]:
                self.state = 323
                self.match(QuerycatParser.T__33)
                self.state = 324
                self.expressionPart()
                pass
            elif token in [35]:
                self.state = 325
                self.match(QuerycatParser.T__34)
                self.state = 326
                self.expressionPart()
                pass
            elif token in [21, 28, 29]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionPartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpression(self):
            return self.getTypedRuleContext(QuerycatParser.PrimaryExpressionContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_expressionPart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionPart" ):
                listener.enterExpressionPart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionPart" ):
                listener.exitExpressionPart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionPart" ):
                return visitor.visitExpressionPart(self)
            else:
                return visitor.visitChildren(self)




    def expressionPart(self):

        localctx = QuerycatParser.ExpressionPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expressionPart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.primaryExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def brackettedExpression(self):
            return self.getTypedRuleContext(QuerycatParser.BrackettedExpressionContext,0)


        def numericLiteral(self):
            return self.getTypedRuleContext(QuerycatParser.NumericLiteralContext,0)


        def booleanLiteral(self):
            return self.getTypedRuleContext(QuerycatParser.BooleanLiteralContext,0)


        def string_(self):
            return self.getTypedRuleContext(QuerycatParser.String_Context,0)


        def var_(self):
            return self.getTypedRuleContext(QuerycatParser.Var_Context,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_primaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = QuerycatParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_primaryExpression)
        try:
            self.state = 336
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.brackettedExpression()
                pass
            elif token in [42, 43, 44, 45, 46, 47, 48, 49, 50]:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.numericLiteral()
                pass
            elif token in [36, 37]:
                self.enterOuterAlt(localctx, 3)
                self.state = 333
                self.booleanLiteral()
                pass
            elif token in [52, 53]:
                self.enterOuterAlt(localctx, 4)
                self.state = 334
                self.string_()
                pass
            elif token in [40, 41]:
                self.enterOuterAlt(localctx, 5)
                self.state = 335
                self.var_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BrackettedExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(QuerycatParser.ExpressionContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_brackettedExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBrackettedExpression" ):
                listener.enterBrackettedExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBrackettedExpression" ):
                listener.exitBrackettedExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBrackettedExpression" ):
                return visitor.visitBrackettedExpression(self)
            else:
                return visitor.visitChildren(self)




    def brackettedExpression(self):

        localctx = QuerycatParser.BrackettedExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_brackettedExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(QuerycatParser.T__19)
            self.state = 339
            self.expression()
            self.state = 340
            self.match(QuerycatParser.T__20)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumericLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numericLiteralUnsigned(self):
            return self.getTypedRuleContext(QuerycatParser.NumericLiteralUnsignedContext,0)


        def numericLiteralPositive(self):
            return self.getTypedRuleContext(QuerycatParser.NumericLiteralPositiveContext,0)


        def numericLiteralNegative(self):
            return self.getTypedRuleContext(QuerycatParser.NumericLiteralNegativeContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_numericLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericLiteral" ):
                listener.enterNumericLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericLiteral" ):
                listener.exitNumericLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericLiteral" ):
                return visitor.visitNumericLiteral(self)
            else:
                return visitor.visitChildren(self)




    def numericLiteral(self):

        localctx = QuerycatParser.NumericLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_numericLiteral)
        try:
            self.state = 345
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42, 43, 44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.numericLiteralUnsigned()
                pass
            elif token in [45, 46, 47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
                self.numericLiteralPositive()
                pass
            elif token in [48, 49, 50]:
                self.enterOuterAlt(localctx, 3)
                self.state = 344
                self.numericLiteralNegative()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumericLiteralUnsignedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(QuerycatParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(QuerycatParser.DECIMAL, 0)

        def DOUBLE(self):
            return self.getToken(QuerycatParser.DOUBLE, 0)

        def getRuleIndex(self):
            return QuerycatParser.RULE_numericLiteralUnsigned

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericLiteralUnsigned" ):
                listener.enterNumericLiteralUnsigned(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericLiteralUnsigned" ):
                listener.exitNumericLiteralUnsigned(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericLiteralUnsigned" ):
                return visitor.visitNumericLiteralUnsigned(self)
            else:
                return visitor.visitChildren(self)




    def numericLiteralUnsigned(self):

        localctx = QuerycatParser.NumericLiteralUnsignedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_numericLiteralUnsigned)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 30786325577728) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumericLiteralPositiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_POSITIVE(self):
            return self.getToken(QuerycatParser.INTEGER_POSITIVE, 0)

        def DECIMAL_POSITIVE(self):
            return self.getToken(QuerycatParser.DECIMAL_POSITIVE, 0)

        def DOUBLE_POSITIVE(self):
            return self.getToken(QuerycatParser.DOUBLE_POSITIVE, 0)

        def getRuleIndex(self):
            return QuerycatParser.RULE_numericLiteralPositive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericLiteralPositive" ):
                listener.enterNumericLiteralPositive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericLiteralPositive" ):
                listener.exitNumericLiteralPositive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericLiteralPositive" ):
                return visitor.visitNumericLiteralPositive(self)
            else:
                return visitor.visitChildren(self)




    def numericLiteralPositive(self):

        localctx = QuerycatParser.NumericLiteralPositiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_numericLiteralPositive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 246290604621824) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumericLiteralNegativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_NEGATIVE(self):
            return self.getToken(QuerycatParser.INTEGER_NEGATIVE, 0)

        def DECIMAL_NEGATIVE(self):
            return self.getToken(QuerycatParser.DECIMAL_NEGATIVE, 0)

        def DOUBLE_NEGATIVE(self):
            return self.getToken(QuerycatParser.DOUBLE_NEGATIVE, 0)

        def getRuleIndex(self):
            return QuerycatParser.RULE_numericLiteralNegative

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericLiteralNegative" ):
                listener.enterNumericLiteralNegative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericLiteralNegative" ):
                listener.exitNumericLiteralNegative(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericLiteralNegative" ):
                return visitor.visitNumericLiteralNegative(self)
            else:
                return visitor.visitChildren(self)




    def numericLiteralNegative(self):

        localctx = QuerycatParser.NumericLiteralNegativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_numericLiteralNegative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 1970324836974592) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QuerycatParser.RULE_booleanLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanLiteral" ):
                listener.enterBooleanLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanLiteral" ):
                listener.exitBooleanLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanLiteral" ):
                return visitor.visitBooleanLiteral(self)
            else:
                return visitor.visitChildren(self)




    def booleanLiteral(self):

        localctx = QuerycatParser.BooleanLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_booleanLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            _la = self._input.LA(1)
            if not(_la==36 or _la==37):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL1(self):
            return self.getToken(QuerycatParser.STRING_LITERAL1, 0)

        def STRING_LITERAL2(self):
            return self.getToken(QuerycatParser.STRING_LITERAL2, 0)

        def getRuleIndex(self):
            return QuerycatParser.RULE_string_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_" ):
                listener.enterString_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_" ):
                listener.exitString_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_" ):
                return visitor.visitString_(self)
            else:
                return visitor.visitChildren(self)




    def string_(self):

        localctx = QuerycatParser.String_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_string_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            _la = self._input.LA(1)
            if not(_la==52 or _la==53):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlankNodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BLANK_NODE_LABEL(self):
            return self.getToken(QuerycatParser.BLANK_NODE_LABEL, 0)

        def ANON(self):
            return self.getToken(QuerycatParser.ANON, 0)

        def getRuleIndex(self):
            return QuerycatParser.RULE_blankNode

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlankNode" ):
                listener.enterBlankNode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlankNode" ):
                listener.exitBlankNode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlankNode" ):
                return visitor.visitBlankNode(self)
            else:
                return visitor.visitChildren(self)




    def blankNode(self):

        localctx = QuerycatParser.BlankNodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_blankNode)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            _la = self._input.LA(1)
            if not(_la==39 or _la==58):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





