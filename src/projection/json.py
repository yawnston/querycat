from typing import List
from querycat.src.querying.instance_model import InstanceCategory
from querycat.src.querying.model import QueryPlan
from querycat.src.querying.schema_model import Max


def instance_to_json(instance: InstanceCategory, query_plan: QueryPlan) -> List[dict]:
    """Given an instance category, convert it to JSON representation.

    Uses an auto-determined root object for the JSON transformation.
    """
    root_var = query_plan.query.select.get_root_var()
    root_schema_obj = [
        x for x in instance.schema_category.objects if x.label == root_var.name
    ][0]

    root_instance_obj = instance.get_object(root_schema_obj.key.value)
    results = []

    for row in root_instance_obj.rows:
        row_result = {}
        is_row_valid = True
        schema_morphisms = [
            x
            for x in instance.schema_category.morphisms
            if x.dom.key.value == root_instance_obj.key.value
        ]
        for morphism in schema_morphisms:
            instance_morphism = instance.get_morphism(morphism.signature.ids[0])
            instance_rows = [
                x
                for x in instance_morphism.mappings
                if x.domain_row.tuples[root_instance_obj.columns[0]]
                == row[0].replace(".0", "")
            ]

            if not instance_rows:
                is_row_valid = False
                continue

            if not morphism.cod.ids[0].signatures[0].ids:
                row_result[morphism.signature.ids[0]] = [
                    next(iter(x.codomain_row.tuples.values())) for x in instance_rows
                ]
                if morphism.max == Max.ONE:
                    row_result[morphism.signature.ids[0]] = row_result[
                        morphism.signature.ids[0]
                    ][0]
            else:
                # TODO: nested objects
                pass

        if is_row_valid:
            results.append(row_result)

    return results
