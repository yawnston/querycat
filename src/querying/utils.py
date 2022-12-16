from querycat.src.parsing.model import Query, Variable
from querycat.src.querying.model import VariableTypes
from querycat.src.querying.schema_model import SchemaCategory


def is_base_morphism(morphism: str) -> bool:
    return "/" not in morphism


def is_dual_morphism(morphism: str) -> bool:
    return "-" in morphism


def get_base_from_dual(morphism: str) -> str:
    return morphism.strip("-").strip()


def get_variable_types(query: Query, schema_category: SchemaCategory) -> VariableTypes:
    variable_types: VariableTypes = {}
    for triple in query.where.triples:
        morphism = schema_category.get_morphism(triple.morphism)
        subject_type = morphism.dom
        object_type = morphism.cod

        if triple.subject.name not in variable_types:
            variable_types[triple.subject.name] = subject_type
        elif variable_types[triple.subject.name] != subject_type:
            raise Exception(f"Variable {triple.subject.name} has conflicting types")

        if isinstance(triple.object, Variable):
            if triple.object.name not in variable_types:
                variable_types[triple.object.name] = object_type
            elif variable_types[triple.object.name] != object_type:
                raise Exception(f"Variable {triple.object.name} has conflicting types")

    return variable_types
