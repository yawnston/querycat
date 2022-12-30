from dataclasses import dataclass
from antlr4 import *
from querycat.src.parsing.antlr_generated.QuerycatLexer import QuerycatLexer
from querycat.src.parsing.antlr_generated.QuerycatParser import QuerycatParser
from querycat.src.parsing.model import Query
from querycat.src.parsing.query_visitor import QueryVisitor


@dataclass
class QueryParser:
    def parse(self, query_string: str) -> Query:
        """Given a MMQL query in the form of a `query_string`,
        parse the query into the internal representation.
        """
        input_stream = InputStream(query_string)
        lexer = QuerycatLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = QuerycatParser(stream)
        tree = parser.query()

        parsedQuery = QueryVisitor().visitQuery(tree)
        return parsedQuery
