from pydantic import BaseModel


class ElasticIndexModel(BaseModel):
    name: str
    body: dict
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True