from session import Base
from sqlalchemy import String, Integer, Column, Sequence
from sqlalchemy.orm import relationship

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, Sequence("role_id_seq"), primary_key=True, index=True)
    name = Column(String(64))
    users = relationship("User", back_populates="roles")