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
        4,1,54,336,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,1,0,
        1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,3,3,104,8,3,1,3,1,3,1,4,
        3,4,109,8,4,1,4,1,4,1,5,1,5,3,5,115,8,5,1,5,1,5,3,5,119,8,5,1,5,
        3,5,122,8,5,1,5,3,5,125,8,5,5,5,127,8,5,10,5,12,5,130,9,5,1,5,1,
        5,1,6,1,6,1,6,3,6,137,8,6,3,6,139,8,6,1,7,1,7,3,7,143,8,7,1,8,1,
        8,1,8,1,9,1,9,1,9,5,9,151,8,9,10,9,12,9,154,9,9,1,10,1,10,1,10,1,
        11,1,11,1,12,1,12,1,12,3,12,164,8,12,3,12,166,8,12,1,13,1,13,1,13,
        1,14,1,14,1,14,1,14,1,14,1,14,3,14,177,8,14,5,14,179,8,14,10,14,
        12,14,182,9,14,1,15,3,15,185,8,15,1,16,1,16,1,16,5,16,190,8,16,10,
        16,12,16,193,9,16,1,17,1,17,1,18,1,18,1,19,1,19,1,19,5,19,202,8,
        19,10,19,12,19,205,9,19,1,20,1,20,3,20,209,8,20,1,21,1,21,1,22,1,
        22,1,22,1,23,1,23,1,24,1,24,3,24,220,8,24,1,25,1,25,1,26,1,26,1,
        26,1,26,3,26,228,8,26,1,27,1,27,1,28,1,28,1,28,5,28,235,8,28,10,
        28,12,28,238,9,28,1,29,1,29,1,29,5,29,243,8,29,10,29,12,29,246,9,
        29,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,
        31,1,31,1,31,3,31,263,8,31,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,
        33,1,33,5,33,274,8,33,10,33,12,33,277,9,33,1,34,1,34,1,34,1,34,1,
        34,5,34,284,8,34,10,34,12,34,287,9,34,1,35,1,35,1,35,1,35,1,35,1,
        35,1,35,3,35,296,8,35,1,36,1,36,1,36,1,36,3,36,302,8,36,1,37,1,37,
        1,37,1,37,1,38,1,38,1,38,1,38,1,38,1,38,1,38,3,38,315,8,38,1,38,
        1,38,1,39,1,39,1,39,3,39,322,8,39,1,40,1,40,1,41,1,41,1,42,1,42,
        1,43,1,43,1,44,1,44,1,45,1,45,1,45,0,0,46,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,0,7,1,0,31,32,1,0,33,
        35,1,0,36,38,1,0,39,41,1,0,27,28,1,0,43,44,2,0,30,30,49,49,335,0,
        92,1,0,0,0,2,95,1,0,0,0,4,98,1,0,0,0,6,101,1,0,0,0,8,108,1,0,0,0,
        10,112,1,0,0,0,12,133,1,0,0,0,14,142,1,0,0,0,16,144,1,0,0,0,18,147,
        1,0,0,0,20,155,1,0,0,0,22,158,1,0,0,0,24,160,1,0,0,0,26,167,1,0,
        0,0,28,170,1,0,0,0,30,184,1,0,0,0,32,186,1,0,0,0,34,194,1,0,0,0,
        36,196,1,0,0,0,38,198,1,0,0,0,40,208,1,0,0,0,42,210,1,0,0,0,44,212,
        1,0,0,0,46,215,1,0,0,0,48,219,1,0,0,0,50,221,1,0,0,0,52,227,1,0,
        0,0,54,229,1,0,0,0,56,231,1,0,0,0,58,239,1,0,0,0,60,247,1,0,0,0,
        62,249,1,0,0,0,64,264,1,0,0,0,66,266,1,0,0,0,68,278,1,0,0,0,70,295,
        1,0,0,0,72,301,1,0,0,0,74,303,1,0,0,0,76,307,1,0,0,0,78,321,1,0,
        0,0,80,323,1,0,0,0,82,325,1,0,0,0,84,327,1,0,0,0,86,329,1,0,0,0,
        88,331,1,0,0,0,90,333,1,0,0,0,92,93,3,2,1,0,93,94,5,0,0,1,94,1,1,
        0,0,0,95,96,3,4,2,0,96,97,3,8,4,0,97,3,1,0,0,0,98,99,5,1,0,0,99,
        100,3,6,3,0,100,5,1,0,0,0,101,103,5,2,0,0,102,104,3,24,12,0,103,
        102,1,0,0,0,103,104,1,0,0,0,104,105,1,0,0,0,105,106,5,3,0,0,106,
        7,1,0,0,0,107,109,5,4,0,0,108,107,1,0,0,0,108,109,1,0,0,0,109,110,
        1,0,0,0,110,111,3,10,5,0,111,9,1,0,0,0,112,114,5,2,0,0,113,115,3,
        12,6,0,114,113,1,0,0,0,114,115,1,0,0,0,115,128,1,0,0,0,116,119,3,
        14,7,0,117,119,3,20,10,0,118,116,1,0,0,0,118,117,1,0,0,0,119,121,
        1,0,0,0,120,122,5,5,0,0,121,120,1,0,0,0,121,122,1,0,0,0,122,124,
        1,0,0,0,123,125,3,12,6,0,124,123,1,0,0,0,124,125,1,0,0,0,125,127,
        1,0,0,0,126,118,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,
        1,0,0,0,129,131,1,0,0,0,130,128,1,0,0,0,131,132,5,3,0,0,132,11,1,
        0,0,0,133,138,3,26,13,0,134,136,5,5,0,0,135,137,3,12,6,0,136,135,
        1,0,0,0,136,137,1,0,0,0,137,139,1,0,0,0,138,134,1,0,0,0,138,139,
        1,0,0,0,139,13,1,0,0,0,140,143,3,16,8,0,141,143,3,18,9,0,142,140,
        1,0,0,0,142,141,1,0,0,0,143,15,1,0,0,0,144,145,5,6,0,0,145,146,3,
        10,5,0,146,17,1,0,0,0,147,152,3,10,5,0,148,149,5,7,0,0,149,151,3,
        10,5,0,150,148,1,0,0,0,151,154,1,0,0,0,152,150,1,0,0,0,152,153,1,
        0,0,0,153,19,1,0,0,0,154,152,1,0,0,0,155,156,5,8,0,0,156,157,3,22,
        11,0,157,21,1,0,0,0,158,159,3,74,37,0,159,23,1,0,0,0,160,165,3,26,
        13,0,161,163,5,5,0,0,162,164,3,24,12,0,163,162,1,0,0,0,163,164,1,
        0,0,0,164,166,1,0,0,0,165,161,1,0,0,0,165,166,1,0,0,0,166,25,1,0,
        0,0,167,168,3,48,24,0,168,169,3,28,14,0,169,27,1,0,0,0,170,171,3,
        36,18,0,171,180,3,32,16,0,172,176,5,9,0,0,173,174,3,36,18,0,174,
        175,3,32,16,0,175,177,1,0,0,0,176,173,1,0,0,0,176,177,1,0,0,0,177,
        179,1,0,0,0,178,172,1,0,0,0,179,182,1,0,0,0,180,178,1,0,0,0,180,
        181,1,0,0,0,181,29,1,0,0,0,182,180,1,0,0,0,183,185,3,28,14,0,184,
        183,1,0,0,0,184,185,1,0,0,0,185,31,1,0,0,0,186,191,3,34,17,0,187,
        188,5,10,0,0,188,190,3,34,17,0,189,187,1,0,0,0,190,193,1,0,0,0,191,
        189,1,0,0,0,191,192,1,0,0,0,192,33,1,0,0,0,193,191,1,0,0,0,194,195,
        3,46,23,0,195,35,1,0,0,0,196,197,3,38,19,0,197,37,1,0,0,0,198,203,
        3,40,20,0,199,200,5,11,0,0,200,202,3,40,20,0,201,199,1,0,0,0,202,
        205,1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,39,1,0,0,0,205,203,
        1,0,0,0,206,209,3,42,21,0,207,209,3,44,22,0,208,206,1,0,0,0,208,
        207,1,0,0,0,209,41,1,0,0,0,210,211,5,29,0,0,211,43,1,0,0,0,212,213,
        5,12,0,0,213,214,3,42,21,0,214,45,1,0,0,0,215,216,3,48,24,0,216,
        47,1,0,0,0,217,220,3,50,25,0,218,220,3,52,26,0,219,217,1,0,0,0,219,
        218,1,0,0,0,220,49,1,0,0,0,221,222,7,0,0,0,222,51,1,0,0,0,223,228,
        3,78,39,0,224,228,3,86,43,0,225,228,3,90,45,0,226,228,5,48,0,0,227,
        223,1,0,0,0,227,224,1,0,0,0,227,225,1,0,0,0,227,226,1,0,0,0,228,
        53,1,0,0,0,229,230,3,56,28,0,230,55,1,0,0,0,231,236,3,58,29,0,232,
        233,5,13,0,0,233,235,3,58,29,0,234,232,1,0,0,0,235,238,1,0,0,0,236,
        234,1,0,0,0,236,237,1,0,0,0,237,57,1,0,0,0,238,236,1,0,0,0,239,244,
        3,60,30,0,240,241,5,14,0,0,241,243,3,60,30,0,242,240,1,0,0,0,243,
        246,1,0,0,0,244,242,1,0,0,0,244,245,1,0,0,0,245,59,1,0,0,0,246,244,
        1,0,0,0,247,248,3,62,31,0,248,61,1,0,0,0,249,262,3,64,32,0,250,251,
        5,15,0,0,251,263,3,64,32,0,252,253,5,16,0,0,253,263,3,64,32,0,254,
        255,5,17,0,0,255,263,3,64,32,0,256,257,5,18,0,0,257,263,3,64,32,
        0,258,259,5,19,0,0,259,263,3,64,32,0,260,261,5,20,0,0,261,263,3,
        64,32,0,262,250,1,0,0,0,262,252,1,0,0,0,262,254,1,0,0,0,262,256,
        1,0,0,0,262,258,1,0,0,0,262,260,1,0,0,0,262,263,1,0,0,0,263,63,1,
        0,0,0,264,265,3,66,33,0,265,65,1,0,0,0,266,275,3,68,34,0,267,268,
        5,21,0,0,268,274,3,68,34,0,269,270,5,12,0,0,270,274,3,68,34,0,271,
        274,3,82,41,0,272,274,3,84,42,0,273,267,1,0,0,0,273,269,1,0,0,0,
        273,271,1,0,0,0,273,272,1,0,0,0,274,277,1,0,0,0,275,273,1,0,0,0,
        275,276,1,0,0,0,276,67,1,0,0,0,277,275,1,0,0,0,278,285,3,70,35,0,
        279,280,5,22,0,0,280,284,3,70,35,0,281,282,5,11,0,0,282,284,3,70,
        35,0,283,279,1,0,0,0,283,281,1,0,0,0,284,287,1,0,0,0,285,283,1,0,
        0,0,285,286,1,0,0,0,286,69,1,0,0,0,287,285,1,0,0,0,288,289,5,23,
        0,0,289,296,3,72,36,0,290,291,5,21,0,0,291,296,3,72,36,0,292,293,
        5,12,0,0,293,296,3,72,36,0,294,296,3,72,36,0,295,288,1,0,0,0,295,
        290,1,0,0,0,295,292,1,0,0,0,295,294,1,0,0,0,296,71,1,0,0,0,297,302,
        3,74,37,0,298,302,3,78,39,0,299,302,3,86,43,0,300,302,3,50,25,0,
        301,297,1,0,0,0,301,298,1,0,0,0,301,299,1,0,0,0,301,300,1,0,0,0,
        302,73,1,0,0,0,303,304,5,24,0,0,304,305,3,54,27,0,305,306,5,25,0,
        0,306,75,1,0,0,0,307,308,5,26,0,0,308,309,5,24,0,0,309,310,3,54,
        27,0,310,311,5,10,0,0,311,314,3,54,27,0,312,313,5,10,0,0,313,315,
        3,54,27,0,314,312,1,0,0,0,314,315,1,0,0,0,315,316,1,0,0,0,316,317,
        5,25,0,0,317,77,1,0,0,0,318,322,3,80,40,0,319,322,3,82,41,0,320,
        322,3,84,42,0,321,318,1,0,0,0,321,319,1,0,0,0,321,320,1,0,0,0,322,
        79,1,0,0,0,323,324,7,1,0,0,324,81,1,0,0,0,325,326,7,2,0,0,326,83,
        1,0,0,0,327,328,7,3,0,0,328,85,1,0,0,0,329,330,7,4,0,0,330,87,1,
        0,0,0,331,332,7,5,0,0,332,89,1,0,0,0,333,334,7,6,0,0,334,91,1,0,
        0,0,32,103,108,114,118,121,124,128,136,138,142,152,163,165,176,180,
        184,191,203,208,219,227,236,244,262,273,275,283,285,295,301,314,
        321
    ]

class QuerycatParser ( Parser ):

    grammarFileName = "Querycat.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'SELECT'", "'{'", "'}'", "'WHERE'", "'.'", 
                     "'OPTIONAL'", "'UNION'", "'FILTER'", "';'", "','", 
                     "'/'", "'-'", "'||'", "'&&'", "'='", "'!='", "'<'", 
                     "'>'", "'<='", "'>='", "'+'", "'*'", "'!'", "'('", 
                     "')'", "'REGEX'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "SCHEMA_MORPHISM", "BLANK_NODE_LABEL", 
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
    RULE_groupGraphPattern = 5
    RULE_triplesBlock = 6
    RULE_graphPatternNotTriples = 7
    RULE_optionalGraphPattern = 8
    RULE_groupOrUnionGraphPattern = 9
    RULE_filter_ = 10
    RULE_constraint = 11
    RULE_selectTriples = 12
    RULE_triplesSameSubject = 13
    RULE_propertyListNotEmpty = 14
    RULE_propertyList = 15
    RULE_objectList = 16
    RULE_object_ = 17
    RULE_verb = 18
    RULE_schemaMorphismOrPath = 19
    RULE_schemaMorphism = 20
    RULE_primaryMorphism = 21
    RULE_dualMorphism = 22
    RULE_graphNode = 23
    RULE_varOrTerm = 24
    RULE_var_ = 25
    RULE_graphTerm = 26
    RULE_expression = 27
    RULE_conditionalOrExpression = 28
    RULE_conditionalAndExpression = 29
    RULE_valueLogical = 30
    RULE_relationalExpression = 31
    RULE_numericExpression = 32
    RULE_additiveExpression = 33
    RULE_multiplicativeExpression = 34
    RULE_unaryExpression = 35
    RULE_primaryExpression = 36
    RULE_brackettedExpression = 37
    RULE_regexExpression = 38
    RULE_numericLiteral = 39
    RULE_numericLiteralUnsigned = 40
    RULE_numericLiteralPositive = 41
    RULE_numericLiteralNegative = 42
    RULE_booleanLiteral = 43
    RULE_string_ = 44
    RULE_blankNode = 45

    ruleNames =  [ "query", "selectQuery", "selectClause", "selectGraphPattern", 
                   "whereClause", "groupGraphPattern", "triplesBlock", "graphPatternNotTriples", 
                   "optionalGraphPattern", "groupOrUnionGraphPattern", "filter_", 
                   "constraint", "selectTriples", "triplesSameSubject", 
                   "propertyListNotEmpty", "propertyList", "objectList", 
                   "object_", "verb", "schemaMorphismOrPath", "schemaMorphism", 
                   "primaryMorphism", "dualMorphism", "graphNode", "varOrTerm", 
                   "var_", "graphTerm", "expression", "conditionalOrExpression", 
                   "conditionalAndExpression", "valueLogical", "relationalExpression", 
                   "numericExpression", "additiveExpression", "multiplicativeExpression", 
                   "unaryExpression", "primaryExpression", "brackettedExpression", 
                   "regexExpression", "numericLiteral", "numericLiteralUnsigned", 
                   "numericLiteralPositive", "numericLiteralNegative", "booleanLiteral", 
                   "string_", "blankNode" ]

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
    SCHEMA_MORPHISM=29
    BLANK_NODE_LABEL=30
    VAR1=31
    VAR2=32
    INTEGER=33
    DECIMAL=34
    DOUBLE=35
    INTEGER_POSITIVE=36
    DECIMAL_POSITIVE=37
    DOUBLE_POSITIVE=38
    INTEGER_NEGATIVE=39
    DECIMAL_NEGATIVE=40
    DOUBLE_NEGATIVE=41
    EXPONENT=42
    STRING_LITERAL1=43
    STRING_LITERAL2=44
    STRING_LITERAL_LONG1=45
    STRING_LITERAL_LONG2=46
    ECHAR=47
    NIL=48
    ANON=49
    PN_CHARS_U=50
    VARNAME=51
    PN_PREFIX=52
    PN_LOCAL=53
    WS=54

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
            self.state = 92
            self.selectQuery()
            self.state = 93
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
            self.state = 95
            self.selectClause()
            self.state = 96
            self.whereClause()
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
            self.state = 98
            self.match(QuerycatParser.T__0)
            self.state = 99
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
            self.state = 101
            self.match(QuerycatParser.T__1)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 848822305554432) != 0:
                self.state = 102
                self.selectTriples()


            self.state = 105
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
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 107
                self.match(QuerycatParser.T__3)


            self.state = 110
            self.groupGraphPattern()
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
        self.enterRule(localctx, 10, self.RULE_groupGraphPattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(QuerycatParser.T__1)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 848822305554432) != 0:
                self.state = 113
                self.triplesBlock()


            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 324) != 0:
                self.state = 118
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2, 6]:
                    self.state = 116
                    self.graphPatternNotTriples()
                    pass
                elif token in [8]:
                    self.state = 117
                    self.filter_()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 120
                    self.match(QuerycatParser.T__4)


                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 848822305554432) != 0:
                    self.state = 123
                    self.triplesBlock()


                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
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
        self.enterRule(localctx, 12, self.RULE_triplesBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.triplesSameSubject()
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 134
                self.match(QuerycatParser.T__4)
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 848822305554432) != 0:
                    self.state = 135
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
        self.enterRule(localctx, 14, self.RULE_graphPatternNotTriples)
        try:
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.optionalGraphPattern()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
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
        self.enterRule(localctx, 16, self.RULE_optionalGraphPattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(QuerycatParser.T__5)
            self.state = 145
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
        self.enterRule(localctx, 18, self.RULE_groupOrUnionGraphPattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.groupGraphPattern()
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 148
                self.match(QuerycatParser.T__6)
                self.state = 149
                self.groupGraphPattern()
                self.state = 154
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
        self.enterRule(localctx, 20, self.RULE_filter_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(QuerycatParser.T__7)
            self.state = 156
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
        self.enterRule(localctx, 22, self.RULE_constraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
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
        self.enterRule(localctx, 24, self.RULE_selectTriples)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.triplesSameSubject()
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 161
                self.match(QuerycatParser.T__4)
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 848822305554432) != 0:
                    self.state = 162
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
        self.enterRule(localctx, 26, self.RULE_triplesSameSubject)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.varOrTerm()
            self.state = 168
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
        self.enterRule(localctx, 28, self.RULE_propertyListNotEmpty)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.verb()
            self.state = 171
            self.objectList()
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 172
                self.match(QuerycatParser.T__8)
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12 or _la==29:
                    self.state = 173
                    self.verb()
                    self.state = 174
                    self.objectList()


                self.state = 182
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
        self.enterRule(localctx, 30, self.RULE_propertyList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12 or _la==29:
                self.state = 183
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
        self.enterRule(localctx, 32, self.RULE_objectList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.object_()
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 187
                self.match(QuerycatParser.T__9)
                self.state = 188
                self.object_()
                self.state = 193
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
        self.enterRule(localctx, 34, self.RULE_object_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
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
        self.enterRule(localctx, 36, self.RULE_verb)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
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
        self.enterRule(localctx, 38, self.RULE_schemaMorphismOrPath)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.schemaMorphism()
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 199
                self.match(QuerycatParser.T__10)
                self.state = 200
                self.schemaMorphism()
                self.state = 205
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
        self.enterRule(localctx, 40, self.RULE_schemaMorphism)
        try:
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.primaryMorphism()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
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
        self.enterRule(localctx, 42, self.RULE_primaryMorphism)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
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
        self.enterRule(localctx, 44, self.RULE_dualMorphism)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(QuerycatParser.T__11)
            self.state = 213
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
        self.enterRule(localctx, 46, self.RULE_graphNode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.varOrTerm()
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


        def graphTerm(self):
            return self.getTypedRuleContext(QuerycatParser.GraphTermContext,0)


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
        self.enterRule(localctx, 48, self.RULE_varOrTerm)
        try:
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.var_()
                pass
            elif token in [27, 28, 30, 33, 34, 35, 36, 37, 38, 39, 40, 41, 48, 49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.graphTerm()
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
        self.enterRule(localctx, 50, self.RULE_var_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            _la = self._input.LA(1)
            if not(_la==31 or _la==32):
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


    class GraphTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numericLiteral(self):
            return self.getTypedRuleContext(QuerycatParser.NumericLiteralContext,0)


        def booleanLiteral(self):
            return self.getTypedRuleContext(QuerycatParser.BooleanLiteralContext,0)


        def blankNode(self):
            return self.getTypedRuleContext(QuerycatParser.BlankNodeContext,0)


        def NIL(self):
            return self.getToken(QuerycatParser.NIL, 0)

        def getRuleIndex(self):
            return QuerycatParser.RULE_graphTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraphTerm" ):
                listener.enterGraphTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraphTerm" ):
                listener.exitGraphTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGraphTerm" ):
                return visitor.visitGraphTerm(self)
            else:
                return visitor.visitChildren(self)




    def graphTerm(self):

        localctx = QuerycatParser.GraphTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_graphTerm)
        try:
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33, 34, 35, 36, 37, 38, 39, 40, 41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.numericLiteral()
                pass
            elif token in [27, 28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.booleanLiteral()
                pass
            elif token in [30, 49]:
                self.enterOuterAlt(localctx, 3)
                self.state = 225
                self.blankNode()
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 4)
                self.state = 226
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
        self.enterRule(localctx, 54, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
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
        self.enterRule(localctx, 56, self.RULE_conditionalOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.conditionalAndExpression()
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 232
                self.match(QuerycatParser.T__12)
                self.state = 233
                self.conditionalAndExpression()
                self.state = 238
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
        self.enterRule(localctx, 58, self.RULE_conditionalAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.valueLogical()
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 240
                self.match(QuerycatParser.T__13)
                self.state = 241
                self.valueLogical()
                self.state = 246
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
        self.enterRule(localctx, 60, self.RULE_valueLogical)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
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

        def numericExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuerycatParser.NumericExpressionContext)
            else:
                return self.getTypedRuleContext(QuerycatParser.NumericExpressionContext,i)


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
        self.enterRule(localctx, 62, self.RULE_relationalExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.numericExpression()
            self.state = 262
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.state = 250
                self.match(QuerycatParser.T__14)
                self.state = 251
                self.numericExpression()
                pass
            elif token in [16]:
                self.state = 252
                self.match(QuerycatParser.T__15)
                self.state = 253
                self.numericExpression()
                pass
            elif token in [17]:
                self.state = 254
                self.match(QuerycatParser.T__16)
                self.state = 255
                self.numericExpression()
                pass
            elif token in [18]:
                self.state = 256
                self.match(QuerycatParser.T__17)
                self.state = 257
                self.numericExpression()
                pass
            elif token in [19]:
                self.state = 258
                self.match(QuerycatParser.T__18)
                self.state = 259
                self.numericExpression()
                pass
            elif token in [20]:
                self.state = 260
                self.match(QuerycatParser.T__19)
                self.state = 261
                self.numericExpression()
                pass
            elif token in [10, 13, 14, 25]:
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


    class NumericExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self):
            return self.getTypedRuleContext(QuerycatParser.AdditiveExpressionContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_numericExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericExpression" ):
                listener.enterNumericExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericExpression" ):
                listener.exitNumericExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericExpression" ):
                return visitor.visitNumericExpression(self)
            else:
                return visitor.visitChildren(self)




    def numericExpression(self):

        localctx = QuerycatParser.NumericExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_numericExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.additiveExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuerycatParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(QuerycatParser.MultiplicativeExpressionContext,i)


        def numericLiteralPositive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuerycatParser.NumericLiteralPositiveContext)
            else:
                return self.getTypedRuleContext(QuerycatParser.NumericLiteralPositiveContext,i)


        def numericLiteralNegative(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuerycatParser.NumericLiteralNegativeContext)
            else:
                return self.getTypedRuleContext(QuerycatParser.NumericLiteralNegativeContext,i)


        def getRuleIndex(self):
            return QuerycatParser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpression(self):

        localctx = QuerycatParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.multiplicativeExpression()
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 4329329135616) != 0:
                self.state = 273
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [21]:
                    self.state = 267
                    self.match(QuerycatParser.T__20)
                    self.state = 268
                    self.multiplicativeExpression()
                    pass
                elif token in [12]:
                    self.state = 269
                    self.match(QuerycatParser.T__11)
                    self.state = 270
                    self.multiplicativeExpression()
                    pass
                elif token in [36, 37, 38]:
                    self.state = 271
                    self.numericLiteralPositive()
                    pass
                elif token in [39, 40, 41]:
                    self.state = 272
                    self.numericLiteralNegative()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 277
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuerycatParser.UnaryExpressionContext)
            else:
                return self.getTypedRuleContext(QuerycatParser.UnaryExpressionContext,i)


        def getRuleIndex(self):
            return QuerycatParser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpression(self):

        localctx = QuerycatParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.unaryExpression()
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11 or _la==22:
                self.state = 283
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [22]:
                    self.state = 279
                    self.match(QuerycatParser.T__21)
                    self.state = 280
                    self.unaryExpression()
                    pass
                elif token in [11]:
                    self.state = 281
                    self.match(QuerycatParser.T__10)
                    self.state = 282
                    self.unaryExpression()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 287
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpression(self):
            return self.getTypedRuleContext(QuerycatParser.PrimaryExpressionContext,0)


        def getRuleIndex(self):
            return QuerycatParser.RULE_unaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpression" ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpression" ):
                listener.exitUnaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpression" ):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpression(self):

        localctx = QuerycatParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_unaryExpression)
        try:
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.match(QuerycatParser.T__22)
                self.state = 289
                self.primaryExpression()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.match(QuerycatParser.T__20)
                self.state = 291
                self.primaryExpression()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 292
                self.match(QuerycatParser.T__11)
                self.state = 293
                self.primaryExpression()
                pass
            elif token in [24, 27, 28, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]:
                self.enterOuterAlt(localctx, 4)
                self.state = 294
                self.primaryExpression()
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
        self.enterRule(localctx, 72, self.RULE_primaryExpression)
        try:
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.brackettedExpression()
                pass
            elif token in [33, 34, 35, 36, 37, 38, 39, 40, 41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.numericLiteral()
                pass
            elif token in [27, 28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 299
                self.booleanLiteral()
                pass
            elif token in [31, 32]:
                self.enterOuterAlt(localctx, 4)
                self.state = 300
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
        self.enterRule(localctx, 74, self.RULE_brackettedExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(QuerycatParser.T__23)
            self.state = 304
            self.expression()
            self.state = 305
            self.match(QuerycatParser.T__24)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RegexExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuerycatParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(QuerycatParser.ExpressionContext,i)


        def getRuleIndex(self):
            return QuerycatParser.RULE_regexExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegexExpression" ):
                listener.enterRegexExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegexExpression" ):
                listener.exitRegexExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegexExpression" ):
                return visitor.visitRegexExpression(self)
            else:
                return visitor.visitChildren(self)




    def regexExpression(self):

        localctx = QuerycatParser.RegexExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_regexExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(QuerycatParser.T__25)
            self.state = 308
            self.match(QuerycatParser.T__23)
            self.state = 309
            self.expression()
            self.state = 310
            self.match(QuerycatParser.T__9)
            self.state = 311
            self.expression()
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 312
                self.match(QuerycatParser.T__9)
                self.state = 313
                self.expression()


            self.state = 316
            self.match(QuerycatParser.T__24)
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
        self.enterRule(localctx, 78, self.RULE_numericLiteral)
        try:
            self.state = 321
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33, 34, 35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.numericLiteralUnsigned()
                pass
            elif token in [36, 37, 38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.numericLiteralPositive()
                pass
            elif token in [39, 40, 41]:
                self.enterOuterAlt(localctx, 3)
                self.state = 320
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
        self.enterRule(localctx, 80, self.RULE_numericLiteralUnsigned)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 60129542144) != 0):
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
        self.enterRule(localctx, 82, self.RULE_numericLiteralPositive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 481036337152) != 0):
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
        self.enterRule(localctx, 84, self.RULE_numericLiteralNegative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 3848290697216) != 0):
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
        self.enterRule(localctx, 86, self.RULE_booleanLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            _la = self._input.LA(1)
            if not(_la==27 or _la==28):
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
        self.enterRule(localctx, 88, self.RULE_string_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            _la = self._input.LA(1)
            if not(_la==43 or _la==44):
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
        self.enterRule(localctx, 90, self.RULE_blankNode)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            _la = self._input.LA(1)
            if not(_la==30 or _la==49):
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





