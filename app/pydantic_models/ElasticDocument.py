from pydantic import BaseModel


class ElasticDocumentModel(BaseModel):
    body: dict
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True