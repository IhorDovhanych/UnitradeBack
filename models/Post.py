from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.orm import relationship
from session import Base
from pydantic import BaseModel
from datetime import datetime


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    title = Column(String(256))
    description = Column(String())
    display = Column(Boolean(), default=True)

    user_id = Column(Integer)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    users = relationship("User", back_populates="roles")


class PostModel(BaseModel):
    title: str
    description: str
    user_id: int

    class Config:
        orm_mode = True


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String(64))

    post_id = Column(Integer)


class CategoryModel(BaseModel):
    name: str
    post_id: int

    class Config:
        orm_mode = True


class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    url = Column(String(256))

    post_id = Column(Integer)


class ImageModel(BaseModel):
    url: str
    post_id: int

    class Config:
        orm_mode = True

