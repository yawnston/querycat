from dataclasses import dataclass
from querycat.src.merging.instance_merger import InstanceMerger
from querycat.src.open_api_definition_client.models.mapping_init import MappingInit

from querycat.src.parsing.model import Triple, Variable
from querycat.src.querying.instance_model import InstanceCategory
from querycat.src.querying.mapping_model import Mapping
from querycat.src.querying.mmcat_client import MMCat
from querycat.src.querying.model import (
    QueryPart,
    QueryPartCompiled,
    QueryPlan,
    VariableTypes,
)
from querycat.src.querying.schema_model import SchemaCategory
from querycat.src.querying.utils import (
    get_variable_types_from_part,
    is_object_terminal,
)
from querycat.src.wrappers.wrapper import Wrapper


@dataclass
class QueryEngine:
    schema_category: SchemaCategory
    mmcat: MMCat

    def compile_statements(self, plan: QueryPlan) -> None:
        new_schema_category = self.mmcat.get_schema_category()
        for part in plan.parts:
            self._compile_query_part(part=part, new_schema_category=new_schema_category)

    def _compile_query_part(
        self, part: QueryPart, new_schema_category: SchemaCategory
    ) -> None:
        variable_types = get_variable_types_from_part(part, self.schema_category)
        wrapper = Wrapper.create(mapping=part.triples_mapping[0][1].mapping)

        self._process_triples(part, variable_types, wrapper)

        # TODO: determining root object id in case of joins, this works only for no joins
        root_kind_mapping = part.triples_mapping[0][1].mapping
        root_object_key = self.schema_category.get_object(
            root_kind_mapping.root_object_id
        ).key
        new_root_object = new_schema_category.get_object_by_key(
            key=root_object_key.value
        )
        mapping_init = MappingInit(
            category_id=self.mmcat.schema_id,
            json_value='{"name": "queryPartKind"}',
            mapping_json_value=Mapping(
                pkey=root_kind_mapping.pkey,
                access_path=wrapper.build_access_path(),
                kind_name=root_kind_mapping.kind_name,
                database=root_kind_mapping.database,
                root_object_id=new_root_object.id,
                root_morphism_id=None,
                category_id=self.mmcat.schema_id,
            ).to_mapping_json_value(),
            root_object_id=new_root_object.id,
            database_id=root_kind_mapping.database.id,
        )
        part.compiled = QueryPartCompiled(
            db_query=wrapper.build_statement(),
            mapping_init=mapping_init,
        )

    def _process_triples(
        self, part: QueryPart, variable_types: VariableTypes, wrapper: Wrapper
    ) -> None:
        for triple, kind in part.triples_mapping:
            subject = triple.subject
            morphism = triple.morphism
            object = triple.object

            if isinstance(object, str):
                raise Exception("Triples with string objects not yet implemented.")
            elif isinstance(object, Variable):
                # TODO: nested properties in Mongo
                if is_object_terminal(variable_types[object.name]):
                    wrapper.add_projection(
                        kind_name=kind.mapping.kind_name,
                        property_name=kind.mapping.get_property_name(morphism),
                        signature=kind.mapping.get_signature(morphism),
                    )

    def _process_filters(self) -> None:
        pass

    def execute_plan(self, plan: QueryPlan) -> InstanceCategory:
        merger = InstanceMerger(mmcat=self.mmcat)
        return merger.merge(query_plan=plan)
