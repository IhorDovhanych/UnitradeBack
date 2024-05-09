from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from core.config import conn_dict


engine = create_engine(
    f"mysql+pymysql://"
    f"{conn_dict['user']}:"
    f"{conn_dict['password']}@"
    f"{conn_dict['host']}:"
    f"{conn_dict['port']}/"
    f"{conn_dict['database']}"
)

sync_session = sessionmaker(bind=engine, class_=Session, expire_on_commit=False, )


class Base(DeclarativeBase):
    pass


def get_session() -> Session:
    db = sync_session()
    try:
        yield db
    finally:
        db.close()
