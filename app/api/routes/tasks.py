from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.task import TaskOut, TaskStatusUpdate, TaskCreate
from app.crud.task import create_task, get_all_tasks, update_task_status

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/", response_model=TaskOut)
def create_task_api(
    payload: TaskCreate,
    db: Session = Depends(get_db),
):
    """Create a new task"""
    try:
        return create_task(db, payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[TaskOut])
def list_tasks(db: Session = Depends(get_db)):
    """Retrieve all tasks"""
    return get_all_tasks(db)


@router.patch("/{task_id}/status", response_model=TaskOut)
def update_task_status_api(
    task_id: int,
    payload: TaskStatusUpdate,
    db: Session = Depends(get_db),
):
    """Update the status of an existing task"""
    try:
        return update_task_status(db, task_id, payload.status)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
