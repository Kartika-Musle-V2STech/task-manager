from app.core.database import engine, Base
import app.models  # IMPORTANT: ensures all models are registered

def init_db():
    Base.metadata.create_all(bind=engine)
