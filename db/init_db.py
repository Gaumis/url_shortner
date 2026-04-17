from db.database import engine, Base
from models.url_model import Base

def init_db():
    Base.metadata.create_all(engine)