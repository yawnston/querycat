from dataclasses import dataclass
from typing import List, Tuple
from uuid import uuid4
from querycat.src.parsing.model import Triple
from querycat.src.querying.instance_model import InstanceCategory
from querycat.src.querying.mapping_model import Signature

from querycat.src.querying.model import QueryPlan
from querycat.src.querying.schema_model import (
    SchemaCategory,
    SchemaMorphism,
    SchemaObject,
)
from querycat.src.querying.utils import (
    calculate_min_max_from_path,
    find_path_in_schema,
    get_variable_types_from_query,
)


@dataclass
class QueryProjector:
    def project(
        self, plan: QueryPlan, where_instance: InstanceCategory
    ) -> Tuple[SchemaCategory, InstanceCategory]:
        self._run_deferred_statements(plan=plan, where_instance=where_instance)
        result_schema = self._create_schema_category(
            plan=plan, where_instance=where_instance
        )
        result_instance = self._project_result(
            plan=plan, where_instance=where_instance, result_schema=result_schema
        )

        return result_schema, result_instance

    def _create_schema_category(
        self, plan: QueryPlan, where_instance: InstanceCategory
    ) -> SchemaCategory:
        result_schema = SchemaCategory(objects=[], morphisms=[])
        for triple in plan.query.select.triples:
            # TODO: implement compound paths in select
            if isinstance(triple.object, str):
                # TODO: implement constant properties
                pass
            else:
                self._create_schema_entities(
                    plan, result_schema, where_instance, triple
                )

        return result_schema

    def _create_schema_entities(
        self,
        plan: QueryPlan,
        result_schema: SchemaCategory,
        where_instance: InstanceCategory,
        triple: Triple,
    ):
        variable_types = get_variable_types_from_query(
            plan.query, where_instance.schema_category
        )
        for var_name in [triple.subject.name, triple.object.name]:
            var_type = variable_types.get(var_name)
            schema_object = result_schema.get_object_by_key(var_type.key.value)
            if not schema_object:
                result_schema.objects.append(
                    SchemaObject(
                        id=var_type.id,
                        ids=var_type.ids,
                        key=var_type.key,
                        label=var_name,
                        super_id=var_type.super_id,
                    )
                )

        schema_morphism = result_schema.get_morphism(triple.morphism)
        if not schema_morphism:
            subject_obj = variable_types.get(triple.subject.name)
            object_obj = variable_types.get(triple.object.name)
            path = find_path_in_schema(
                source_key=subject_obj.key.value,
                dest_key=object_obj.key.value,
                schema_category=where_instance.schema_category,
            )
            min, max = calculate_min_max_from_path(path)
            result_schema.morphisms.append(
                SchemaMorphism(
                    id=uuid4().hex,
                    min=min,
                    max=max,
                    signature=Signature(ids=[triple.morphism], is_null=False),
                    dom=subject_obj,
                    cod=object_obj,
                )
            )

    def _run_deferred_statements(
        self, plan: QueryPlan, where_instance: InstanceCategory
    ):
        # TODO: implement deferred statements
        pass

    def _project_result(
        self,
        plan: QueryPlan,
        where_instance: InstanceCategory,
        result_schema: SchemaCategory,
    ) -> InstanceCategory:
        ...
