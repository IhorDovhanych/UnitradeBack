from main import app
from . import Role, User
from .PostsRouter import PostsRouter
from .ReportsRouter import ReportsRouter

app.include_router(User.router, prefix='/api/user', tags=["User"])
app.include_router(Role.router, prefix='/api/role', tags=["Role"])
app.include_router(PostsRouter)
app.include_router(ReportsRouter)

import elastic.routers
import auth.routers