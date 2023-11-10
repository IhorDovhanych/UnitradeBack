from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, Text
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
    user_id = Column(Integer, ForeignKey("users.id"))

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    users = relationship("User", back_populates="posts")
    reports = relationship("Report", back_populates="posts")
    categories = relationship("Category", back_populates="posts")
    images = relationship("Image", back_populates="posts")

    # def __str__(self):
    #     return f"{self.title}: \n{self.description}"


class PostModel(BaseModel):
    title: str
    description: str
    user_id: int

    # class Config:
    #     orm_mode = True


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String(64))

    post_id = Column(Integer, ForeignKey("posts.id"))
    posts = relationship("Post", back_populates="categories")


# class CategoryModel(BaseModel):
#     name: str
#     post_id: int
#
#     class Config:
#         orm_mode = True


class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    url = Column(String(256))

    post_id = Column(Integer, ForeignKey("posts.id"))
    posts = relationship("Post", back_populates="images")


# class ImageModel(BaseModel):
#     url: str
#     post_id: int
#
#     class Config:
#         orm_mode = True

