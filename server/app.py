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


# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["application"]
# mycol = mydb["users"]
# mycol.create_index("user_index")

# query_builder = ElasticsearchAPIQueryBuilder()

# es = Elasticsearch(["mongodb://localhost:27017/Users.user_collection"])
# es = Elasticsearch()

# wait_elasticsearch(es)
# index_name = "user_index"


# @query_builder.filter()
# def filter_category(c: Optional[str] = Query(None)):
#     return {
#         "term": {
#             "category": c
#         }
#     } if c is not None else None


# @query_builder.matcher()
# def match_fields(q: Optional[str] = Query(None)):
#     return {
#         "multi_match": {
#             "query": q,
#             "fuzziness": "AUTO",
#             "fields": [
#                 "name^2",
#                 "description"
#             ]
#         }
#     } if q is not None else None


# @query_builder.sorter()
# def sort_by(direction: Optional[str] = Query(None)):
#     return {
#         "name": direction
#     } if direction is not None else None


# @query_builder.highlighter()
# def highlight(q: Optional[str] = Query(None),
#               h: bool = Query(False)):
#     return {
#         "name": {}
#     } if q is not None and h else None

# # import pymongo

# @app.get("/search")
# async def search(query_body: Dict = Depends(query_builder.build())) -> JSONResponse:
#     # Search using the Elasticsearch client.
#     return es.search(
#         body=query_body,
#         index=index_name
#     )

# @app.get("/search")
# async def search(query_para : Esearch):
#     query_str = jsonable_encoder(query_para).get("user_query")
#     print(query_str)
#     # Search using the Elasticsearch client.
#     myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#     db = myclient["application"]
#     # mycol = db["users"]
#     asd = db.users.find( { "$email": { "$search": query_str } } )
#     import pdb
#     pdb.set_trace()
#     for doc in asd:
#         print(doc)

#     print(jsonable_encoder(asd))
#     return jsonable_encoder(asd)


# def elastic_user():
#     users = []
#     for user in user_collection.find():
#         users.append(user_helper(user))
#     return users

# usr = elastic_user()
# print(usr)
# usrs_list = retrieve_users()
# print(usrs_list)

# for usr in usrs_list:
#     print(usr)

# import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# #use database "organisation"
# mydb = myclient['application']
# col = mydb['users']
# print("List of collections\n--------------------")
# #list the collections
# for coll in mydb.list_collection_names():
#     print(coll)
# import pdb
# pdb.set_trace()

es = Elasticsearch(HOST="http://localhost", PORT=9200)

mongoclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongoclient.Users
collection = db["users_collection"]
cursor = collection.find({})

loop = 0
for user in cursor:
    user = user_helper(user)
    es.index(index="user_index", doc_type="text", id=loop, body=user)
    loop +=1
    print(type(user))

@app.get("/search")
async def search(query_para : Esearch):
    query_str = jsonable_encoder(query_para).get("user_query")
    print(query_str)
    es.index(index="query_index", doc_type="text", id=loop, body=query_str)

