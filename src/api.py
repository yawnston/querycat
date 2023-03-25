from typing import List
from uuid import uuid4
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

from querycat.src.quecat import SchemaObjectInfo, create_query_plans, execute_query_json
from querycat.src.querying.model import QueryPlan


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SCHEMA_ID = 4
MMCAT_BASE_URL = "http://localhost:27500"


query_result_dict = {}
query_plans_dict = {}


class QueryBody(BaseModel):
    query_string: str


class QueryResult(BaseModel):
    id: str
    results: List[dict]


@app.post("/query/execute")
def execute_query_endpoint(query: QueryBody) -> QueryResult:
    query_results = execute_query_json(
        query_string=query.query_string,
        schema_id=SCHEMA_ID,
        mmcat_base_url=MMCAT_BASE_URL,
    )
    result_id = uuid4().hex
    query_result_dict[result_id] = QueryResult(id=result_id, results=query_results)

    return query_result_dict[result_id]


@app.get("/query/{result_id}")
def get_query_result(result_id) -> QueryResult:
    return query_result_dict[result_id]


class QueryPlanView(BaseModel):
    cost: int
    compiled: List[str]


class QueryPlanInfo(BaseModel):
    plan: QueryPlanView
    object_info: List[SchemaObjectInfo]


class QueryPlansResult(BaseModel):
    id: str
    infos: List[QueryPlanInfo]


@app.post("/query/plans")
def post_create_query_plans(query: QueryBody):
    plans, obj_infos = create_query_plans(
        query_string=query.query_string,
        schema_id=SCHEMA_ID,
        mmcat_base_url=MMCAT_BASE_URL,
    )

    results: List[QueryPlanInfo] = []
    for i in range(len(plans)):
        results.append(
            QueryPlanInfo(
                plan=QueryPlanView(
                    cost=plans[i].cost,
                    compiled=[x.compiled.db_query for x in plans[i].parts],
                ),
                object_info=obj_infos[i],
            )
        )

    result_id = uuid4().hex
    query_plans_dict[result_id] = QueryPlansResult(id=result_id, infos=results)
    return query_plans_dict[result_id]


@app.get("/query/plans/{result_id}")
def get_plans_info(result_id):
    return query_plans_dict[result_id]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
