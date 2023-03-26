from typing import List
from uuid import uuid4
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

from querycat.src.quecat import execute_query_json
from querycat.src.ui_helpers import SchemaObjectInfo, create_query_plans


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

SCHEMA_ID = 481
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


@app.post("/query/execute/{plan_id}")
def execute_query_endpoint(plan_id: str) -> QueryResult:
    plans_result_id, plan_num = plan_id.split("_")
    plan_query: str = query_plans_dict[plans_result_id].query
    query_results = execute_query_json(
        query_string=plan_query,
        schema_id=SCHEMA_ID,
        mmcat_base_url=MMCAT_BASE_URL,
        plan_num=int(plan_num),
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
    query: str
    infos: List[QueryPlanInfo]


@app.post("/query/plans")
def post_create_query_plans(query: QueryBody):
    plans, obj_infos = create_query_plans(
        query_string=query.query_string,
        schema_id=SCHEMA_ID,
        mmcat_base_url=MMCAT_BASE_URL,
        get_db_info=True,
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
    query_plans_dict[result_id] = QueryPlansResult(
        id=result_id, infos=results, query=query.query_string
    )
    return query_plans_dict[result_id]


@app.post("/query/objectinfo")
def post_query_object_info(query: QueryBody):
    try:
        plans, obj_infos = create_query_plans(
            query_string=query.query_string,
            schema_id=SCHEMA_ID,
            mmcat_base_url=MMCAT_BASE_URL,
            get_db_info=False,
        )
    except Exception as e:
        print(e)
        return QueryPlansResult(id="dummy_id", infos=[])

    results: List[QueryPlanInfo] = []
    for i in range(len(plans)):
        results.append(
            QueryPlanInfo(
                plan=QueryPlanView(
                    cost=plans[i].cost,
                    compiled=[
                        x.compiled.db_query if x.compiled is not None else ""
                        for x in plans[i].parts
                    ],
                ),
                object_info=obj_infos[i],
            )
        )

    result_id = uuid4().hex
    query_plans_dict[result_id] = QueryPlansResult(
        id=result_id, infos=results, query=query.query_string
    )
    return query_plans_dict[result_id]


@app.get("/query/plans/{result_id}")
def get_plans_info(result_id):
    return query_plans_dict[result_id]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
