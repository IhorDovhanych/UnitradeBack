from main import app
from . import Role, User
from .PostsRouter import PostsRouter
from .ReportsRouter import ReportsRouter

app.include_router(User.router, prefix='/user')
app.include_router(Role.router, prefix='/role')
app.include_router(PostsRouter)
app.include_router(ReportsRouter)
