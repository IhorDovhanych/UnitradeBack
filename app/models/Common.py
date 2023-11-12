from sqlalchemy import Column, DateTime
from core.session import Base
from datetime import datetime


class CreateUpdateBase:
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
