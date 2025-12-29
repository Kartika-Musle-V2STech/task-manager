from app.core.database import SessionLocal

def get_db():
    """Provide a database session to API routes"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()