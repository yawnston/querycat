from querycat.src.querying.query_visitor import QueryVisitor

from antlr4 import *
from querycat.src.querying.antlr_generated.QuerycatParser import QuerycatParser
from querycat.src.querying.antlr_generated.QuerycatLexer import QuerycatLexer


class QueryParser:
    def parse(self, query_string: str):
        input_stream = InputStream(query_string)
        lexer = QuerycatLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = QuerycatParser(stream)
        tree = parser.query()

        ast = QueryVisitor().visitQuery(tree)
        return ast
