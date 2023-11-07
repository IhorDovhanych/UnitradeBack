from fastapi import FastAPI
from routes import User, Role

app = FastAPI()

@app.get('/')
def test2():
    return "test"

app.include_router(User.router, prefix='/user')
app.include_router(Role.router, prefix='/role')