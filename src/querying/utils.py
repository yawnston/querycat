from typing import List, Tuple
from querycat.src.parsing.model import Query, Triple, Variable
from querycat.src.querying.mapping_model import Signature
from querycat.src.querying.model import QueryPart, VariableTypes
from querycat.src.querying.schema_model import (
    Id,
    Max,
    Min,
    SchemaCategory,
    SchemaMorphism,
    SchemaObject,
)


def is_base_morphism(morphism: str) -> bool:
    return "/" not in morphism


def is_dual_morphism(morphism: str) -> bool:
    return "-" in morphism


def get_base_from_dual(morphism: str) -> str:
    return morphism.strip("-").strip()


def get_variable_types_from_query(
    query: Query, schema_category: SchemaCategory
) -> VariableTypes:
    """Get the set of variables from the query, along with
    the corresponding schema object for each variable.
    """
    return get_variable_types(
        triples=query.where.triples, schema_category=schema_category
    )


def get_variable_types_from_part(
    part: QueryPart, schema_category: SchemaCategory
) -> VariableTypes:
    """Get the set of variables from the query part, along with
    the corresponding schema object for each variable.
    """
    return get_variable_types(
        triples=[triple for triple, _ in part.triples_mapping],
        schema_category=schema_category,
    )


def get_variable_types(
    triples: List[Triple],
    schema_category: SchemaCategory,
) -> VariableTypes:
    """Get the set of variables from the provided set of triples,
    along with the corresponding schema object for each variable.
    """
    variable_types: VariableTypes = {}
    for triple in triples:
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


def is_object_terminal(object: SchemaObject) -> bool:
    return object.ids == [Id(signatures=[Signature(ids=[], is_null=False)])]


def find_path_in_schema(
    source_key: int, dest_key: int, schema_category: SchemaCategory
) -> List[SchemaMorphism]:
    """Given the key of a source and destination schema object,
    find a path between them in the schema category, and return
    the list of schema morphisms along this path.
    """
    # TODO: reverse morphism traversals
    source = schema_category.get_object_by_key(source_key)
    dest = schema_category.get_object_by_key(dest_key)

    find_queue = [[x] for x in schema_category.morphisms if x.dom == source]
    while find_queue:
        current_path = find_queue.pop()
        if current_path[-1].cod == dest:
            return current_path

        new_traversals = [
            x for x in schema_category.morphisms if x.dom == current_path[-1].cod
        ]
        for new_traversal in new_traversals:
            # Only prolong traversal if we would not hit a cycle
            if abs(new_traversal.signature.ids[0]) not in [
                abs(x.signature.ids[0]) for x in current_path
            ]:
                find_queue.append(current_path + [new_traversal])

    raise Exception("No path found in schema category.")


def calculate_min_max_from_path(path: List[SchemaMorphism]) -> Tuple[Min, Max]:
    # TODO: reverse morphism traversals
    min = Min.ZERO if Min.ZERO in [x.min for x in path] else Min.ONE
    max = Max.ONE if Max.ONE in [x.max for x in path] else Max.STAR

    return min, max
