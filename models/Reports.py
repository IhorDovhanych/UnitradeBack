from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from session import Base
from pydantic import BaseModel
from datetime import datetime


class Report(Base):
    __tablename__ = 'reports'
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    title = Column(String(256))
    description = Column(Text())

    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    users = relationship("User", back_populates="reports")
    posts = relationship("Post", back_populates="reports")


class ReportModel(BaseModel):
    title: str
    description: str
    user_id: int
    post_id: int

    class Config:
        orm_mode = True
