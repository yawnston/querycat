from dataclasses import dataclass
from enum import Enum
import json
from typing import Dict, List, Tuple
from querycat.src.querying.model import VariableNameMap

from querycat.src.wrappers.wrapper import Projection, Wrapper, WrapperError


class MongodbWrapperError(WrapperError):
    pass


class MongodbComparisonOperator(str, Enum):
    EQUALS = "$eq"
    NOT_EQUALS = "$ne"
    LESS_THAN = "$lt"
    LESS_THAN_EQUALS = "$lte"
    GREATER_THAN = "$gt"
    GREATER_THAN_EQUALS = "$gte"


@dataclass
class MongodbWrapper(Wrapper):
    def __init__(self):
        super().__init__()

    def is_join_supported(self) -> bool:
        return False

    def is_optional_join_supported(self) -> bool:
        return True

    def is_non_id_filter_supported(self) -> bool:
        return True

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

        pipeline.append(self._build_const_filters())
        pipeline.extend(self._build_var_filters())
        pipeline.append(self._build_projection())

        return pipeline

    def _build_projection(self) -> Dict:
        projection_names = [
            self._get_var_name(projection) for projection in self._projections
        ]

        # We support nested complex properties even for arrays, but MM-evocat
        # does not support them yet, so their querying will not work.
        project = {name: 1 for name in projection_names}

        return {"$project": project}

    def _build_const_filters(self) -> Dict:
        filters = {}

        for constant_filter in self._constant_filters:
            projection = [
                x
                for x in self._projections
                if x.variable_id == constant_filter.variable_id
            ][0]
            prop_name = projection.property_path[-1].name.value

            operator_name = constant_filter.operator.name
            if not operator_name in MongodbComparisonOperator.__members__:
                raise MongodbWrapperError(
                    f"Comparison operator {constant_filter.operator} is not supported by MongoDB!"
                )
            native_operator: str = MongodbComparisonOperator[operator_name].value

            filters[prop_name] = {native_operator: constant_filter.constant}

        for values in self._values_filters:
            projection = [
                x for x in self._projections if x.variable_id == values.variable_id
            ][0]
            prop_name = projection.property_path[-1].name.value

            if not values.constants:
                raise MongodbWrapperError(
                    f"VALUES clause for variable {prop_name} has no allowed values."
                )

            filters[prop_name] = {"$in": values.constants}

        return {"$match": filters}

    def _build_var_filters(self) -> List[Dict]:
        filter_stages = []

        for filter in self._variables_filters:
            lhs_projection = [
                x for x in self._projections if x.variable_id == filter.lhs_variable_id
            ][0]
            lhs_prop_name = self._get_var_name(lhs_projection)
            rhs_projection = [
                x for x in self._projections if x.variable_id == filter.rhs_variable_id
            ][0]
            rhs_prop_name = self._get_var_name(rhs_projection)

            operator_name = filter.operator.name
            if not operator_name in MongodbComparisonOperator.__members__:
                raise MongodbWrapperError(
                    f"Comparison operator {filter.operator} is not supported by MongoDB!"
                )
            native_operator: str = MongodbComparisonOperator[operator_name].value

            filter_stages.append(
                {"$match": {"$expr": {native_operator: [lhs_prop_name, rhs_prop_name]}}}
            )

        return filter_stages

    def _build_var_name_map(self) -> VariableNameMap:
        return {x.variable_id: self._get_var_name_path(x) for x in self._projections}

    def _get_var_name(self, projection: Projection) -> str:
        return ".".join(self._get_var_name_path(projection))

    def _get_var_name_path(self, projection: Projection) -> List[str]:
        return [x.name.value for x in projection.property_path]
