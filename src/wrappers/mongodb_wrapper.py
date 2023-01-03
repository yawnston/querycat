from dataclasses import dataclass
import json
from typing import Dict, List, Tuple
from querycat.src.querying.model import VariableNameMap

from querycat.src.wrappers.wrapper import Projection, Wrapper


class MongodbWrapperError(Exception):
    pass


@dataclass
class MongodbWrapper(Wrapper):
    def __init__(self):
        super().__init__()

    def build_statement(self) -> Tuple[str, VariableNameMap]:
        query = "db."
        query += self._base_collection_name()

        aggregation_pipeline = self._build_aggregation_pipeline()
        query += f".aggregate({json.dumps(aggregation_pipeline)})"
        var_name_map = self._build_var_name_map()
        return query, var_name_map

    def _base_collection_name(self) -> str:
        base_collection = None
        kind_names = {
            self._kinds[projection.kind_id] for projection in self._projections
        }
        for kind_name in kind_names:
            if base_collection is None:
                base_collection = kind_name
            else:
                raise MongodbWrapperError(
                    "Joining collections in MongoDB is not supported since MM-evocat does not support it!"
                )

        if base_collection is None:
            raise MongodbWrapperError("No collection to aggregate on.")
        return base_collection

    def _build_aggregation_pipeline(self) -> List:
        pipeline = []

        pipeline.append(self._build_projection())

        return pipeline

    def _build_projection(self) -> Dict:
        project = {
            projection.property_path[-1].name.value: 1
            for projection in self._projections
        }

        return {"$project": project}

    def _build_var_name_map(self) -> VariableNameMap:
        return {x.variable_id: [self._get_var_name(x)] for x in self._projections}

    def _get_var_name(self, projection: Projection) -> str:
        return projection.property_path[-1].name.value
