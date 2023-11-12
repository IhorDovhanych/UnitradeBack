from core.session import Base
from sqlalchemy import String, Integer, Column, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType
from .Common import CreateUpdateBase


class User(Base, CreateUpdateBase):
    __tablename__ = "users"
    id = Column(Numeric(precision=32, scale=0), primary_key=True, index=True)
    name = Column(String(256))
    email = Column(EmailType(length=128), unique=True)
    picture = Column(String(256))

    role_id = Column(Integer, ForeignKey("roles.id"))
    roles = relationship("Role", back_populates="users")

    posts = relationship("Post", back_populates="users")
    reports = relationship("Report", back_populates="users")
