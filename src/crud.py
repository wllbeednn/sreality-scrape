from typing import Type

from models import Flat
from sqlalchemy.orm import Session


def get_all(db: Session) -> list[Type[Flat]]:
    return db.query(Flat).all()


def create(db: Session, title, image_url) -> Flat:
    db_obj = Flat(title=title, image_url=image_url)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
