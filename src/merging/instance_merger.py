from dataclasses import dataclass
from querycat.src.querying.instance_model import InstanceCategory

from querycat.src.querying.mmcat_client import MMCat
from querycat.src.querying.model import QueryPlan


@dataclass
class InstanceMerger:
    mmcat: MMCat

    def merge(self, query_plan: QueryPlan) -> InstanceCategory:
        """Given a `query_plan` whose query parts have already been compiled,
        send each native query to MM-evocat for execution, merge the results
        into a single instance category and return it.

        Note that the returned instance category is lazy because of the API
        of MM-evocat - it can only return the data for a single instance
        object or morphism at a time as an API response. For this reason,
        the instance category retrieves data if it does not yet have it,
        and then caches the result to eliminate extra API calls.
        """
        for part in query_plan.parts:
            mapping_id = self.mmcat.create_mapping(part.compiled.mapping_init)
            self.mmcat.run_job_with_query(
                query=part.compiled.db_query, mapping_id=mapping_id
            )

        # Return instance category with no data - it will be filled in
        # automatically when the data is needed.
        return InstanceCategory(
            mmcat=self.mmcat, schema_category=self.mmcat.get_schema_category()
        )
