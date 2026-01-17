from app.core.database import engine, Base
import app.core.models  

def init_db():
    """Initialize the database by creating all tables."""
    Base.metadata.create_all(bind=engine)
