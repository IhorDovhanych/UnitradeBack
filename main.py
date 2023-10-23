from fastapi import FastAPI, Depends
from pydantic import BaseModel
import pymysql.cursors
from sqlalchemy.orm import Session
from session import get_session

app = FastAPI()
connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='unitrade_db',
    port=3310,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
@app.get('/test')
def test():
    with connection:
        with connection.cursor() as cursor:
            sql = f"""
                SELECT * FROM text;
                """
            cursor.execute(sql)
            result = cursor.fetchall() 
        connection.commit()
        return result