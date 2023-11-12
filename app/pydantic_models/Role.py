from pydantic import BaseModel

class RoleModel(BaseModel):
    name: str

    class Config:
        orm_mode = True