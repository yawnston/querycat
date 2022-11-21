from antlr4 import *
from querycat.src.querying.antlr_generated.QuerycatLexer import QuerycatLexer
from querycat.src.querying.antlr_generated.QuerycatParser import QuerycatParser
from querycat.src.querying.model import Query
from querycat.src.querying.query_visitor import QueryVisitor


class QueryParser:
    def parse(self, query_string: str) -> Query:
        input_stream = InputStream(query_string)
        lexer = QuerycatLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = QuerycatParser(stream)
        tree = parser.query()

        ast = QueryVisitor().visitQuery(tree)
        return ast
