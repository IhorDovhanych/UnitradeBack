from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.orm import relationship
from session import Base
from pydantic import BaseModel
from datetime import datetime


class Report(Base):
    __tablename__ = 'reports'
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    title = Column(String(256))
    description = Column(String())

    user_id = Column(Integer)
    post_id = Column(Integer)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    users = relationship("User", back_populates="roles")


class PostModel(BaseModel):
    title: str
    description: str
    user_id: int
    post_id: int

    class Config:
        orm_mode = True
