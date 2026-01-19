"""
API routes for Tasks and Task Types
"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

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
async def list_tasks(db: AsyncSession = Depends(get_db)):
    """Retrieve all tasks"""
    return await get_all_tasks(db)


@router.post(
    "/",
    response_model=TaskOut,
    summary="Create task",
)
async def create_task_api(
    payload: TaskCreate,
    db: AsyncSession = Depends(get_db),
):
    """Create a new task"""
    return await create_task(db, payload)


@router.patch(
    "/{task_id}/status",
    response_model=TaskOut,
    summary="Update task status",
)
async def update_task_status_api(
    task_id: int,
    payload: TaskStatusUpdate,
    db: AsyncSession = Depends(get_db),
):
    """Update the status of an existing task"""
    return await update_task_status(db, task_id, payload.status)


# TASK TYPES


@router.get(
    "/types",
    response_model=list[TaskTypeOut],
    summary="List task types",
)
async def list_task_types(db: AsyncSession = Depends(get_db)):
    """Retrieve all task types"""
    return await get_all_task_types(db)
