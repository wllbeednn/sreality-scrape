"""
Module for ORM models.
"""
from db.base_class import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class Flat(Base):
    """
    Represents flat table in the database.
    """
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String, nullable=False)
    image_url = Column(String, nullable=True)
