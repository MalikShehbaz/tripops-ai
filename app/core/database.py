from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.core.config import settings


engine = create_engine(settings.database_url)

LocalSession = sessionmaker(
    bind=engine,
    autocommit= False,
    autoflush= False,
)

class Base(DeclarativeBase):
    pass

def get_db():
    db = LocalSession()

    try:
        yield db
    finally:
        db.close()