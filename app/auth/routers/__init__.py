from auth.routers import AuthRouter
from main import app

app.include_router(AuthRouter.router, prefix='/auth', tags=["Auth"])