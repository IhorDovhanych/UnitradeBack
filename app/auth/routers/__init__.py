from auth.routers import Auth
from main import app

app.include_router(Auth.router, prefix='/auth', tags=["Auth"])