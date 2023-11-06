from sqlalchemy.orm import declarative_base
Base = declarative_base()

from .role import Role
from .user import User