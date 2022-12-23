# Connection string for MongoDB instance to use for experiments.
# Connection string should include database name!
EXPERIMENTS_MONGODB_CONNECTION_STRING = "mongodb://mmcat_user:mmcat_password@localhost:5446/mmcat_server_data?authSource=admin"

EXPERIMENTS_MONGODB_COLLECTION_NAME = "experiments_orders"

EXPERIMENTS_POSTGRESQL_CONNECTION_STRING = "postgresql://mmcat_user:mmcat_password@localhost:5445/mmcat_server_data"

EXPERIMENTS_POSTGRESQL_TABLE_NAME = "experiments_customers"

# Number of order objects in MongoDB to use in experiments
EXPERIMENTS_MONGODB_NUM_ORDERS = 6000

# Number of customer objects in PostgreSQL to use in experiments
EXPERIMENTS_POSTGRESQL_NUM_CUSTOMERS = 2000

# Schema category to use for the experiments
EXPERIMENTS_SCHEMA_CATEGORY_JSON = """{"objects": [{"temporaryId": 208, "position": {"x": 78.0, "y": 130.0}, "jsonValue": "{\\"ids\\": [{\\"signatures\\": [{\\"ids\\": [1], \\"isNull\\": false}]}], \\"key\\": {\\"value\\": 1}, \\"label\\": \\"Customer\\", \\"superId\\": {\\"signatures\\": [{\\"ids\\": [1], \\"isNull\\": false}]}}"}, {"temporaryId": 209, "position": {"x": 74.0, "y": 4.0}, "jsonValue": "{\\"ids\\": [{\\"signatures\\": [{\\"ids\\": [], \\"isNull\\": false}]}], \\"key\\": {\\"value\\": 2}, \\"label\\": \\"Id\\", \\"superId\\": {\\"signatures\\": [{\\"ids\\": [], \\"isNull\\": false}]}}"}, {"temporaryId": 210, "position": {"x": -91.0, "y": 9.0}, "jsonValue": "{\\"ids\\": [{\\"signatures\\": [{\\"ids\\": [], \\"isNull\\": false}]}], \\"key\\": {\\"value\\": 3}, \\"label\\": \\"Name\\", \\"superId\\": {\\"signatures\\": [{\\"ids\\": [], \\"isNull\\": false}]}}"}, {"temporaryId": 211, "position": {"x": -93.0, "y": 132.0}, "jsonValue": "{\\"ids\\": [{\\"signatures\\": [{\\"ids\\": [], \\"isNull\\": false}]}], \\"key\\": {\\"value\\": 4}, \\"label\\": \\"Surname\\", \\"superId\\": {\\"signatures\\": [{\\"ids\\": [], \\"isNull\\": false}]}}"}, {"temporaryId": 212, "position": {"x": -90.0, "y": 263.0}, "jsonValue": "{\\"ids\\": [{\\"signatures\\": [{\\"ids\\": [], \\"isNull\\": false}]}], \\"key\\": {\\"value\\": 5}, \\"label\\": \\"Address\\", \\"superId\\": {\\"signatures\\": [{\\"ids\\": [], \\"isNull\\": false}]}}"}, {"temporaryId": 213, "position": {"x": 370.0, "y": 133.0}, "jsonValue": "{\\"ids\\": [{\\"signatures\\": [{\\"ids\\": [6], \\"isNull\\": false}]}], \\"key\\": {\\"value\\": 6}, \\"label\\": \\"Order\\", \\"superId\\": {\\"signatures\\": [{\\"ids\\": [6], \\"isNull\\": false}]}}"}, {"temporaryId": 214, "position": {"x": 370.0, "y": -4.0}, "jsonValue": "{\\"ids\\": [{\\"signatures\\": [{\\"ids\\": [], \\"isNull\\": false}]}], \\"key\\": {\\"value\\": 7}, \\"label\\": \\"Id\\", \\"superId\\": {\\"signatures\\": [{\\"ids\\": [], \\"isNull\\": false}]}}"}, {"temporaryId": 215, "position": {"x": 520.0, "y": -6.0}, "jsonValue": "{\\"ids\\": [{\\"signatures\\": [{\\"ids\\": [], \\"isNull\\": false}]}], \\"key\\": {\\"value\\": 8}, \\"label\\": \\"TotalPrice\\", \\"superId\\": {\\"signatures\\": [{\\"ids\\": [], \\"isNull\\": false}]}}"}, {"temporaryId": 216, "position": {"x": 520.0, "y": 135.0}, "jsonValue": "{\\"ids\\": [{\\"signatures\\": [{\\"ids\\": [], \\"isNull\\": false}]}], \\"key\\": {\\"value\\": 9}, \\"label\\": \\"Status\\", \\"superId\\": {\\"signatures\\": [{\\"ids\\": [], \\"isNull\\": false}]}}"}], "morphisms": [{"temporaryDomId": 208, "temporaryCodId": 209, "jsonValue": "{\\"max\\": \\"ONE\\", \\"min\\": \\"ONE\\", \\"signature\\": {\\"ids\\": [1], \\"isNull\\": false}}"}, {"temporaryDomId": 209, "temporaryCodId": 208, "jsonValue": "{\\"max\\": \\"ONE\\", \\"min\\": \\"ONE\\", \\"signature\\": {\\"ids\\": [-1], \\"isNull\\": false}}"}, {"temporaryDomId": 208, "temporaryCodId": 210, "jsonValue": "{\\"max\\": \\"ONE\\", \\"min\\": \\"ONE\\", \\"signature\\": {\\"ids\\": [2], \\"isNull\\": false}}"}, {"temporaryDomId": 210, "temporaryCodId": 208, "jsonValue": "{\\"max\\": \\"STAR\\", \\"min\\": \\"ZERO\\", \\"signature\\": {\\"ids\\": [-2], \\"isNull\\": false}}"}, {"temporaryDomId": 208, "temporaryCodId": 211, "jsonValue": "{\\"max\\": \\"ONE\\", \\"min\\": \\"ONE\\", \\"signature\\": {\\"ids\\": [3], \\"isNull\\": false}}"}, {"temporaryDomId": 211, "temporaryCodId": 208, "jsonValue": "{\\"max\\": \\"STAR\\", \\"min\\": \\"ZERO\\", \\"signature\\": {\\"ids\\": [-3], \\"isNull\\": false}}"}, {"temporaryDomId": 208, "temporaryCodId": 212, "jsonValue": "{\\"max\\": \\"ONE\\", \\"min\\": \\"ONE\\", \\"signature\\": {\\"ids\\": [4], \\"isNull\\": false}}"}, {"temporaryDomId": 212, "temporaryCodId": 208, "jsonValue": "{\\"max\\": \\"STAR\\", \\"min\\": \\"ZERO\\", \\"signature\\": {\\"ids\\": [-4], \\"isNull\\": false}}"}, {"temporaryDomId": 213, "temporaryCodId": 208, "jsonValue": "{\\"max\\": \\"ONE\\", \\"min\\": \\"ONE\\", \\"signature\\": {\\"ids\\": [5], \\"isNull\\": false}}"}, {"temporaryDomId": 208, "temporaryCodId": 213, "jsonValue": "{\\"max\\": \\"STAR\\", \\"min\\": \\"ZERO\\", \\"signature\\": {\\"ids\\": [-5], \\"isNull\\": false}}"}, {"temporaryDomId": 213, "temporaryCodId": 214, "jsonValue": "{\\"max\\": \\"ONE\\", \\"min\\": \\"ONE\\", \\"signature\\": {\\"ids\\": [6], \\"isNull\\": false}}"}, {"temporaryDomId": 214, "temporaryCodId": 213, "jsonValue": "{\\"max\\": \\"ONE\\", \\"min\\": \\"ONE\\", \\"signature\\": {\\"ids\\": [-6], \\"isNull\\": false}}"}, {"temporaryDomId": 213, "temporaryCodId": 215, "jsonValue": "{\\"max\\": \\"ONE\\", \\"min\\": \\"ONE\\", \\"signature\\": {\\"ids\\": [7], \\"isNull\\": false}}"}, {"temporaryDomId": 215, "temporaryCodId": 213, "jsonValue": "{\\"max\\": \\"STAR\\", \\"min\\": \\"ZERO\\", \\"signature\\": {\\"ids\\": [-7], \\"isNull\\": false}}"}, {"temporaryDomId": 213, "temporaryCodId": 216, "jsonValue": "{\\"max\\": \\"ONE\\", \\"min\\": \\"ONE\\", \\"signature\\": {\\"ids\\": [8], \\"isNull\\": false}}"}, {"temporaryDomId": 216, "temporaryCodId": 213, "jsonValue": "{\\"max\\": \\"STAR\\", \\"min\\": \\"ZERO\\", \\"signature\\": {\\"ids\\": [-8], \\"isNull\\": false}}"}]}"""

EXPERIMENTS_MONGODB_ROOT_OBJECT_KEY = 6

EXPERIMENTS_MONGODB_MAPPING_JSON = """{"databaseId":1,"categoryId":17,"rootObjectId":213,"jsonValue":"{\\"name\\":\\"Order<MongoDB>\\"}","mappingJsonValue":"{\\"kindName\\":\\"experiments_orders\\",\\"pkey\\":[],\\"accessPath\\":{\\"_class\\":\\"ComplexProperty\\",\\"name\\":{\\"_class\\":\\"StaticName\\",\\"value\\":\\"experiments_orders\\",\\"type\\":\\"STATIC_NAME\\"},\\"signature\\":{\\"ids\\":[0],\\"isNull\\":true},\\"subpaths\\":[{\\"_class\\":\\"SimpleProperty\\",\\"name\\":{\\"_class\\":\\"StaticName\\",\\"value\\":\\"_id\\",\\"type\\":\\"STATIC_NAME\\"},\\"value\\":{\\"signature\\":{\\"ids\\":[6],\\"isNull\\":false}}},{\\"_class\\":\\"SimpleProperty\\",\\"name\\":{\\"_class\\":\\"StaticName\\",\\"value\\":\\"total_price\\",\\"type\\":\\"STATIC_NAME\\"},\\"value\\":{\\"signature\\":{\\"ids\\":[7],\\"isNull\\":false}}},{\\"_class\\":\\"SimpleProperty\\",\\"name\\":{\\"_class\\":\\"StaticName\\",\\"value\\":\\"status\\",\\"type\\":\\"STATIC_NAME\\"},\\"value\\":{\\"signature\\":{\\"ids\\":[8],\\"isNull\\":false}}},{\\"_class\\":\\"SimpleProperty\\",\\"name\\":{\\"_class\\":\\"StaticName\\",\\"value\\":\\"customer_id\\",\\"type\\":\\"STATIC_NAME\\"},\\"value\\":{\\"signature\\":{\\"ids\\":[1,5],\\"isNull\\":false}}}]}}"}"""

EXPERIMENTS_POSTGRESQL_ROOT_OBJECT_KEY = 1

EXPERIMENTS_POSTGRESQL_MAPPING_JSON = """{"databaseId":2,"categoryId":17,"rootObjectId":208,"jsonValue":"{\\"name\\":\\"Customer<PostgreSQL>\\"}","mappingJsonValue":"{\\"kindName\\":\\"experiments_customers\\",\\"pkey\\":[],\\"accessPath\\":{\\"_class\\":\\"ComplexProperty\\",\\"name\\":{\\"_class\\":\\"StaticName\\",\\"value\\":\\"experiments_customers\\",\\"type\\":\\"STATIC_NAME\\"},\\"signature\\":{\\"ids\\":[0],\\"isNull\\":true},\\"subpaths\\":[{\\"_class\\":\\"SimpleProperty\\",\\"name\\":{\\"_class\\":\\"StaticName\\",\\"value\\":\\"id\\",\\"type\\":\\"STATIC_NAME\\"},\\"value\\":{\\"signature\\":{\\"ids\\":[1],\\"isNull\\":false}}},{\\"_class\\":\\"SimpleProperty\\",\\"name\\":{\\"_class\\":\\"StaticName\\",\\"value\\":\\"name\\",\\"type\\":\\"STATIC_NAME\\"},\\"value\\":{\\"signature\\":{\\"ids\\":[2],\\"isNull\\":false}}},{\\"_class\\":\\"SimpleProperty\\",\\"name\\":{\\"_class\\":\\"StaticName\\",\\"value\\":\\"surname\\",\\"type\\":\\"STATIC_NAME\\"},\\"value\\":{\\"signature\\":{\\"ids\\":[3],\\"isNull\\":false}}},{\\"_class\\":\\"SimpleProperty\\",\\"name\\":{\\"_class\\":\\"StaticName\\",\\"value\\":\\"address\\",\\"type\\":\\"STATIC_NAME\\"},\\"value\\":{\\"signature\\":{\\"ids\\":[4],\\"isNull\\":false}}}]}}"}"""
