.PHONY: antlr-generate

# Generate an up-to-date parset, lexer and visitor from the Querycat.g4 grammar
antlr-generate:
	antlr4 -Dlanguage=Python3 -visitor -o src/querying/antlr_generated/ -Xexact-output-dir -Werror grammars/Querycat.g4

openapi-generate:
	cd src/ && openapi-python-client generate --meta "none" --url http://localhost:27500/v3/api-docs
