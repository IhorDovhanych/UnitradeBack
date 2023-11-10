from pydantic import BaseModel, EmailStr


class UserModel(BaseModel):
    name: str
    password: str
    email: EmailStr
    jwt_token: str
    role_id: int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
