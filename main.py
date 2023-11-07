from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def test2():
    return "test"

import routes