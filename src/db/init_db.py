"""
Module for initializing database
"""
from db.base_class import Base
from db.session import engine


def init_db() -> None:
    """
    Initialize database. Create tables for all models if they are not created.
    Note, that in database tables may not be created instantly, only after some crud operation.
    """
    Base.metadata.create_all(bind=engine)
