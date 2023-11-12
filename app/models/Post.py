from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, Text, Numeric
from sqlalchemy.orm import relationship
from core.session import Base
from pydantic import BaseModel
from datetime import datetime


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    title = Column(String(256))
    description = Column(Text())
    display = Column(Boolean(), default=True)
    user_id = Column(Numeric(precision=32, scale=0), ForeignKey("users.id"))

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    users = relationship("User", back_populates="posts")
    reports = relationship("Report", back_populates="posts")
    categories = relationship("Category", back_populates="posts")
    images = relationship("Image", back_populates="posts")


class PostModel(BaseModel):
    title: str
    description: str
    display: bool = True
    user_id: int


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String(64))

    post_id = Column(Integer, ForeignKey("posts.id"))
    posts = relationship("Post", back_populates="categories")


class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    url = Column(String(256))

    post_id = Column(Integer, ForeignKey("posts.id"))
    posts = relationship("Post", back_populates="images")
