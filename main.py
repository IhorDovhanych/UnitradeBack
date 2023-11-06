from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
#from session import get_session

app = FastAPI()

@app.get('/')
def test2():
    return "test"

