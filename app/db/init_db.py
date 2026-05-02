from app.db.db import engine
from app.db.base import Base

# Import all models here
from app.models import complaint, defect

def init_db():
    Base.metadata.create_all(bind=engine)