from main import app
from . import RoleRouter, UserRouter, ReportsRouter, PostsRouter

app.include_router(UserRouter.router, prefix='/api/user', tags=["User"])
app.include_router(RoleRouter.router, prefix='/api/role', tags=["Role"])
app.include_router(PostsRouter.router, prefix="/api/posts", tags=["Posts"])
app.include_router(ReportsRouter.router, prefix="/api/reports", tags=["Reports"])

import elastic.routers
import auth.routers