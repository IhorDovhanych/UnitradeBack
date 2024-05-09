from pydantic import BaseModel, EmailStr


class UserModel(BaseModel):
    id: int
    name: str
    email: EmailStr
    role_id: int
    picture: str
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
