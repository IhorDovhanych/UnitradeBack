from core.session import Base
from sqlalchemy import String, Integer, Column, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType
import datetime


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String(256))
    password = Column(String(128))
    email = Column(EmailType(length=128), unique=True)
    jwt_token = Column(String(256))
    role_id = Column(Integer, ForeignKey("roles.id"))
    roles = relationship("Role", back_populates="users")

    posts = relationship("Post", back_populates="users")
    reports = relationship("Report", back_populates="users")

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow
    )

