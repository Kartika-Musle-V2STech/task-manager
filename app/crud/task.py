"""CRUD Operations for Tasks and Task Types"""

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.core.models import Task, TaskType, TaskStatusEnum
from app.core.exceptions import BadRequestException, NotFoundException
from app.schemas.task import TaskCreate

# TASK CRUD


def create_task(db: Session, task_in: TaskCreate) -> Task:
    """Create a new task"""
    task = Task(
        title=task_in.title,
        project_id=task_in.project_id,
        type_id=task_in.type_id,
        status=TaskStatusEnum.PENDING,  # enforce default here
        priority=task_in.priority,
    )

    db.add(task)

    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise BadRequestException("Invalid project, type, or priority value") from exc

    db.refresh(task)
    return task


def get_task_by_id(db: Session, task_id: int) -> Task:
    """Fetch a task by its ID"""
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise NotFoundException("Task not found")

    return task


def get_tasks_by_project(db: Session, project_id: int) -> list[Task]:
    """Fetch all tasks belonging to a project"""
    return db.query(Task).filter(Task.project_id == project_id).all()


def get_all_tasks(db: Session) -> list[Task]:
    """Fetch all tasks"""
    return db.query(Task).all()


def update_task_status(
    db: Session,
    task_id: int,
    status: TaskStatusEnum,
) -> Task:
    """Update only the status of a task"""

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise NotFoundException("Task not found")

    task.status = status

    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise BadRequestException("Invalid status value") from exc

    db.refresh(task)
    return task


# TASK TYPE CRUD


def get_all_task_types(db: Session) -> list[TaskType]:
    """Return all task types"""
    return db.query(TaskType).order_by(TaskType.id).all()
