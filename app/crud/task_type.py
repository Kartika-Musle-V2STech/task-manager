from sqlalchemy.orm import Session
from app.models.task_type import TaskType

def get_all_task_types(db:Session):
    """
    Returns all task types
    """
    return db.query(TaskType).order_by(TaskType.id).all()
