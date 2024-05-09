from pydantic import BaseModel


class DocumentModel(BaseModel):
    body: dict
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True