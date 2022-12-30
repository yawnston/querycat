from dataclasses import dataclass
from querycat.src.querying.instance_model import InstanceCategory

from querycat.src.querying.mmcat_client import MMCat
from querycat.src.querying.model import QueryPlan


@dataclass
class InstanceMerger:
    mmcat: MMCat

    def merge(self, query_plan: QueryPlan) -> InstanceCategory:
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

    def merge_test(self, query_plan: QueryPlan):
        pg_query = """SELECT id, name, surname, address_id FROM customer"""
        pg_query = """SELECT customer.id AS id, name, surname, address.id AS address_id FROM customer INNER JOIN address ON customer.address_id = address.id"""
        pg_query2 = """SELECT customer.id AS id, name, surname, address.id AS address_id, address.street as address_street FROM customer INNER JOIN address ON customer.address_id = address.id"""
        # pg_query2 = """SELECT id, street, city, postal_code FROM address"""
        # pg_query = """SELECT customer.id AS customerId, customer.name AS customerName, customer.surname AS customerSurname, address.id AS addressId, address.street AS addressStreet FROM customer INNER JOIN address ON customer.address_id = address.id"""
        # pg_query = """SELECT customer.id AS a, customer.name AS b, customer.surname AS c, address.id AS d, address.street AS e FROM customer INNER JOIN address ON customer.address_id = address.id"""
        mongo_query = """db.order.aggregate( [ { $project : { "_id": 1, "customer_id": 1, "items": 1 } } ] )"""

        self.mmcat.run_job_with_query(query=pg_query2, mapping_id=23)
        # self.mmcat.run_job_with_query(query=mongo_query, mapping_id=17)

        x = self.mmcat.get_instance_object(object_key=5)
        y = self.mmcat.get_instance_object(object_key=7)
        w = self.mmcat.get_instance_morphism(signature=5)
        z = self.mmcat.get_instance_morphism(signature=4)

        pass


if __name__ == "__main__":
    merger = InstanceMerger(
        mmcat=MMCat(schema_id=11, base_url="http://localhost:27500")
    )
    merger.merge_test(None)
