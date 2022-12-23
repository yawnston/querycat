from dataclasses import dataclass
from datetime import datetime
from typing import List, Tuple
from uuid import uuid4
from querycat.src.parsing.model import Triple
from querycat.src.querying.instance_model import (
    InstanceCategory,
    InstanceMorphism,
    InstanceObject,
    MappingRow,
)
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
        """Given a `WHERE` instance category and the schema category
        induced by the `SELECT` clause, project the data to the final
        instance category for the `SELECT` clause.
        """
        result_instance = InstanceCategory(mmcat=None, schema_category=result_schema)

        for new_schema_obj in result_schema.objects:
            instance_obj = where_instance.get_object(key=new_schema_obj.key.value)
            result_instance._objects[new_schema_obj.key.value] = InstanceObject(
                key=new_schema_obj.key,
                columns=instance_obj.columns,
                rows=instance_obj.rows,
            )

        for new_schema_morphism in result_schema.morphisms:
            path = find_path_in_schema(
                source_key=new_schema_morphism.dom.key.value,
                dest_key=new_schema_morphism.cod.key.value,
                schema_category=where_instance.schema_category,
            )

            instance_path = [
                where_instance.get_morphism(x.signature.ids[0]) for x in path
            ]

            while len(instance_path) > 1:
                b = instance_path.pop()
                a = instance_path.pop()
                start_time = datetime.now()
                contraction = self._contract_morphisms(a, b)
                end_time = datetime.now()
                print(
                    f"Morphism contraction time elapsed: {(end_time - start_time).total_seconds()} seconds."
                )
                instance_path.append(contraction)

            final_morphism = instance_path[0]
            signature = new_schema_morphism.signature.ids[0]
            result_instance._morphisms[signature] = InstanceMorphism(
                signature=signature,
                mappings=final_morphism.mappings,
            )

        return result_instance

    def _contract_morphisms(
        self, a: InstanceMorphism, b: InstanceMorphism
    ) -> InstanceMorphism:
        """Given morphisms (x)-a->(y)-b->(z), create a morphism
        (x)-c->(z) via contraction.
        """
        contraction_rows: List[MappingRow] = []
        for a_row in a.mappings:
            join_rows = [
                x.codomain_row for x in b.mappings if x.domain_row == a_row.codomain_row
            ]
            for b_codomain_row in join_rows:
                contraction_rows.append(
                    MappingRow(domain_row=a_row.domain_row, codomain_row=b_codomain_row)
                )

        return InstanceMorphism(signature=0, mappings=contraction_rows)
