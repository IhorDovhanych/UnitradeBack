from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from .config import conn_dict

engine = create_engine(
    f"mysql+pymysql://{conn_dict['user']}:{conn_dict['password']}"
    f"@{conn_dict['host']}:{conn_dict['port']}/{conn_dict['database']}"
)
sync_session = sessionmaker(bind=engine, class_=Session, expire_on_commit=False, )


class Base(DeclarativeBase):
    pass


# @contextmanager
def get_session() -> Session:
    db = sync_session()
    try:
        yield db
    finally:
        db.close()