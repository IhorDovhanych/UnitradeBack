from session import Base
from sqlalchemy import String, Integer, Column, Sequence
from sqlalchemy.orm import relationship
from pydantic import BaseModel

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String(64))
    users = relationship("User", back_populates="roles")
    
class RoleModel(BaseModel):
    name: str
    class Config:
        orm_mode = True