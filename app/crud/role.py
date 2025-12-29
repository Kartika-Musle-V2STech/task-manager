from sqlalchemy.orm import Session
from app.models.role import Role

def get_all_roles(db: Session):
    """
    Returns all roles.
    Used for dropdowns and read-only listings.
    """
    return db.query(Role).order_by(Role.id).all()
    

