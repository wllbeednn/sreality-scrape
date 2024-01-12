"""
Module with SQLAlchemy base class used to create other models from this Base class.
"""

from sqlalchemy.orm import as_declarative, declared_attr


# Base class is managed by SQLAlchemy and doesn't need more public methods
@as_declarative()
class Base:
    """
    Base class of all ORM mapped models.
    """

    __name__: str

    # Generate __tablename__ automatically
    @declared_attr  # type: ignore
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
