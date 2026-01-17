"""
API routes for Tasks and Task Types
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.task import (
    TaskCreate,
    TaskOut,
    TaskStatusUpdate,
    TaskTypeOut,
)
from app.crud.task import (
    create_task,
    get_all_tasks,
    update_task_status,
    get_all_task_types,
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


# TASKS


@router.get(
    "/",
    response_model=list[TaskOut],
    summary="List tasks",
)
def list_tasks(db: Session = Depends(get_db)):
    """Retrieve all tasks"""
    return get_all_tasks(db)


@router.post(
    "/",
    response_model=TaskOut,
    summary="Create task",
)
def create_task_api(
    payload: TaskCreate,
    db: Session = Depends(get_db),
):
    """Create a new task"""
    return create_task(db, payload)


@router.patch(
    "/{task_id}/status",
    response_model=TaskOut,
    summary="Update task status",
)
def update_task_status_api(
    task_id: int,
    payload: TaskStatusUpdate,
    db: Session = Depends(get_db),
):
    """Update the status of an existing task"""
    return update_task_status(db, task_id, payload.status)


# TASK TYPES


@router.get(
    "/types",
    response_model=list[TaskTypeOut],
    summary="List task types",
)
def list_task_types(db: Session = Depends(get_db)):
    """Retrieve all task types"""
    return get_all_task_types(db)
