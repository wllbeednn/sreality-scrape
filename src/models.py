from db.base_class import Base
from sqlalchemy import Column, String


class Flat(Base):
    title = Column(String, nullable=False)
    image_url = Column(String, nullable=True)
