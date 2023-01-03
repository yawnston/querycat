from dataclasses import dataclass
from querycat.src.merging.instance_merger import InstanceMerger

from querycat.src.parsing.model import Filter, Values, Variable
from querycat.src.querying.instance_model import InstanceCategory
from querycat.src.querying.mapping_builder import MappingBuilder
from querycat.src.querying.mapping_model import SimpleProperty
from querycat.src.querying.mmcat_client import MMCat
from querycat.src.querying.model import (
    QueryPart,
    QueryPartCompiled,
    QueryPlan,
    VariableTypes,
)
from querycat.src.querying.schema_model import SchemaCategory
from querycat.src.querying.utils import (
    get_kind_id,
    get_kinds_from_part,
    get_variable_id,
    get_variable_types_from_part,
    is_object_terminal,
)
from querycat.src.wrappers.wrapper import Wrapper


@dataclass
class QueryEngine:
    """Query engine class which is responsible for the translation of
    query parts into native queries, and the subsequent execution
    of those query parts.
    """

    schema_category: SchemaCategory
    mmcat: MMCat

    def compile_statements(self, plan: QueryPlan) -> None:
        """For each query part in the given query plan, compile the corresponding
        native database query, as well as the required mapping for the output
        of this query.

        This method saves the compiled queries within each query part, which is why
        it returns `None`.
        """
        where_schema_category = self.mmcat.get_schema_category()
        for part in plan.parts:
            self._compile_query_part(
                part=part, where_schema_category=where_schema_category
            )

    def _compile_query_part(
        self, part: QueryPart, where_schema_category: SchemaCategory
    ) -> None:
        variable_types = get_variable_types_from_part(part, self.schema_category)
        wrapper = Wrapper.create(mapping=part.triples_mapping[0][1].mapping)
        mapping_builder = MappingBuilder(
            schema_category=self.schema_category,
            where_schema_category=where_schema_category,
        )

        for kind in get_kinds_from_part(part):
            wrapper.define_kind(get_kind_id(kind), kind.mapping.kind_name)

        self._process_triples(part, variable_types, wrapper, mapping_builder)
        self._process_filters(part, wrapper)
        self._process_values(part, wrapper)

        native_query, var_name_map = wrapper.build_statement()
        mapping_init = mapping_builder.build_mapping(var_name_map)

        part.compiled = QueryPartCompiled(
            db_query=native_query,
            mapping_init=mapping_init,
        )

    def _process_triples(
        self,
        part: QueryPart,
        variable_types: VariableTypes,
        wrapper: Wrapper,
        mapping_builder: MappingBuilder,
    ) -> None:
        for triple, kind in part.triples_mapping:
            subject = triple.subject
            morphism = triple.morphism
            object = triple.object

            if isinstance(object, str):
                raise Exception("Triples with string objects not yet implemented.")
            elif isinstance(object, Variable):
                if is_object_terminal(variable_types[object.name]):
                    property_path = [
                        x
                        for x in kind.mapping.access_path.subpaths
                        if isinstance(x, SimpleProperty)
                        and x.value.signature.ids[0] == int(morphism)
                    ]
                    wrapper.add_projection(
                        property_path=property_path,
                        kind_id=get_kind_id(kind),
                        variable_id=get_variable_id(object),
                    )
                    mapping_builder.define_variable(
                        variable_id=get_variable_id(object),
                        property_path=property_path,
                        mapping=kind.mapping,
                    )

    def _process_filters(
        self,
        part: QueryPart,
        wrapper: Wrapper,
    ) -> None:
        filters = (filter for filter in part.statements if isinstance(filter, Filter))
        for filter in filters:
            if isinstance(filter.lhs, Variable):
                if isinstance(filter.rhs, str):
                    wrapper.add_constant_filter(
                        variable_id=get_variable_id(filter.lhs),
                        operator=filter.operator,
                        constant=filter.rhs,
                    )

    def _process_values(
        self,
        part: QueryPart,
        wrapper: Wrapper,
    ) -> None:
        values_filters = (
            values for values in part.statements if isinstance(values, Values)
        )
        for values in values_filters:
            wrapper.add_values_filter(
                variable_id=get_variable_id(values.variable),
                constants=values.allowed_values,
            )

    def execute_plan(self, plan: QueryPlan) -> InstanceCategory:
        """Given a query plan with a compiled native query for each
        of its query parts, execute these native statements and save
        their results in an instance category in MM-evocat, returning
        this instance category.

        Note that the result instance category corresponds to the results
        of the query's `WHERE` clause, not the entire query.
        """
        merger = InstanceMerger(mmcat=self.mmcat)
        return merger.merge(query_plan=plan)
