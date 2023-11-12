from main import app
from . import Role, User

app.include_router(User.router, prefix='/user', tags=["User"])
app.include_router(Role.router, prefix='/role', tags=["Role"])
