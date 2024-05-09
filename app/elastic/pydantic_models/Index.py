from pydantic import BaseModel


class IndexModel(BaseModel):
    name: str
    body: dict
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True