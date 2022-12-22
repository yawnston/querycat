from dataclasses import dataclass
import json
from typing import Dict, List
from querycat.src.querying.mapping_model import (
    ComplexProperty,
    Signature,
    SimpleProperty,
    SimpleValue,
    StaticName,
)

from querycat.src.wrappers.wrapper import Wrapper


class MongodbWrapperError(Exception):
    pass


@dataclass
class MongodbWrapper(Wrapper):
    def __init__(self):
        super().__init__()

    def build_statement(self) -> str:
        query = "db."
        query += self._base_collection_name()

        aggregation_pipeline = self._build_aggregation_pipeline()
        query += f".aggregate({json.dumps(aggregation_pipeline)})"
        return query

    def _base_collection_name(self) -> str:
        base_collection = None
        kind_names = {projection.kind_name for projection in self._projections}
        for kind_name in kind_names:
            if base_collection is None:
                base_collection = kind_name
            else:
                raise Exception(
                    "Joining collections in MongoDB is not yet implemented!"
                )

        if base_collection is None:
            raise MongodbWrapperError("No collection to aggregate on.")
        return base_collection

    def _build_aggregation_pipeline(self) -> List:
        pipeline = []

        pipeline.append(self._build_projection())

        return pipeline

    def _build_projection(self) -> Dict:
        # TODO: nested properties
        project = {projection.property_name: 1 for projection in self._projections}

        return {"$project": project}

    def build_access_path(self) -> ComplexProperty:
        # TODO: more complex access paths, joins
        # TODO: implement
        subpaths = [
            SimpleProperty(
                name=StaticName(value="_id"),
                value=SimpleValue(signature=Signature(ids=[10], is_null=False)),
            ),
            SimpleProperty(
                name=StaticName(value="customer_id"),
                value=SimpleValue(signature=Signature(ids=[1, 9], is_null=False)),
            ),
        ]
        root = ComplexProperty(
            name=StaticName(value="root"),
            signature=Signature(ids=[0], is_null=True),
            subpaths=subpaths,
        )
        return root