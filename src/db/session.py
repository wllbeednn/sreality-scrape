"""
Module which includes classes and methods responsible for connection to database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator

# postgres://user:pass@localhost:5432
postgres_database_uri = "postgresql://dev:pass@db:5432/devdb"

engine = create_engine(postgres_database_uri, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, None, None]:
    """
    Generates database connections provided by Session class.
    :return: yields database session which will be automatically closed after request is satisfied.
    """
    with SessionLocal() as db:
        yield db
