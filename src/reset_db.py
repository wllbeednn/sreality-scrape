"""
Script to reset database.
"""
from db import Base
from db.session import engine
from models import Flat
from sqlalchemy.exc import SQLAlchemyError
import time
import logging

try:
    Base.metadata.drop_all(engine)
except SQLAlchemyError as e:
    # probably docker container with db is not initialized, just wait a little bit
    logging.warning(msg="Probably db is not yet initialized, sleeping for a moment.")

    time.sleep(7)
    Base.metadata.drop_all(engine)
