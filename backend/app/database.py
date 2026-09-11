from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings


class Base(DeclarativeBase):
    pass


engine = create_engine(settings.database_url) if settings.database_url else None
SessionLocal = sessionmaker(bind=engine) if engine else None
