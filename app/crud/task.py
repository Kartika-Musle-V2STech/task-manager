from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models.task import Task
from app.schemas.task import TaskCreate


def create_task(db: Session, task_in: TaskCreate) -> Task:
    """Create a new task"""
    task = Task(
        title=task_in.title,
        project_id=task_in.project_id,
        type_id=task_in.type_id,
        status=task_in.status,
        priority=task_in.priority,
    )

    db.add(task)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("Invalid project, type or enum value")

    db.refresh(task)
    return task


def get_task_by_id(db: Session, task_id: int) -> Task | None:
    """Fetch a task by its ID"""
    return db.query(Task).filter(Task.id == task_id).first()


def get_tasks_by_project(db: Session, project_id: int) -> list[Task]:
    """Fetch all tasks belonging to a project"""
    return db.query(Task).filter(Task.project_id == project_id).all()


def get_all_tasks(db: Session) -> list[Task]:
    """Fetch all tasks"""
    return db.query(Task).all()

def update_task_status(db: Session, task_id: int, status: str) -> Task:
    """ Update only the status of a task"""
  
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise ValueError("Task not found")
    
    task.status = status
    
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("Invalid staus_id")
    
    db.refresh(task)
    return task
