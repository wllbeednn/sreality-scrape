from db import Base
from db.session import engine
from models import Flat

Base.metadata.drop_all(engine)
