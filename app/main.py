from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pymysql
import pymysql.cursors
from core.config import conn_dict
from elasticsearch import AsyncElasticsearch

app = FastAPI()
elastic_client = AsyncElasticsearch("http://localhost:9200")
app.state.elastic_client = elastic_client

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def test2():
    return "test, use /docs for swagger"


import routers
import show_useful_links