import json
import re
from fastapi import Depends, FastAPI, Query
from fastapi_elasticsearch.utils import wait_elasticsearch
from fastapi_elasticsearch import ElasticsearchAPIQueryBuilder
from elasticsearch import Elasticsearch
from .models.search import Esearch
from fastapi.encoders import jsonable_encoder
from typing import Dict, Optional
from starlette.responses import JSONResponse
from .database import *
import pymongo
from server.routes.user import router as UserRouter
from bson.json_util import loads, dumps


app = FastAPI()

app.include_router(UserRouter, tags=["User"], prefix="/user")


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to this fantastic app!"}


# es = Elasticsearch(HOST="http://localhost", PORT=9200)

# mongoclient = pymongo.MongoClient("mongodb://localhost:27017/")
# db = mongoclient.Users
# collection = db["users_collection"]
# cursor = collection.find({})

# loop = 0
# for user in cursor:
#     user = user_helper(user)
#     es.index(index="user_index", id=loop, body=user)
#     loop += 1
#     print(type(user))

# res = es.get(index="user_index", doc_type="text", id=1)
# # print(res["_source"])
# # print(res)

# doc_1 = {"sentence":"ak"}
# es.index(index="english", doc_type="sentences", id=1, body=doc_1)


# @app.get("/search")
# async def search(query_para: Esearch):
#     query_str = jsonable_encoder(query_para).get("user_query")
#     # es.index(index="query_index", doc_type="text", id=loop, body=query_str)
#     print(query_str)
#     import pdb
#     pdb.set_trace()
