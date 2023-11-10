from core.session import Base
from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import relationship


class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String(64))
    users = relationship("User", back_populates="roles")

