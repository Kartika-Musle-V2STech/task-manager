"""
CRUD Operations for Tasks and Task Types (Async)
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.core.models import Task, TaskType, TaskStatusEnum
from app.core.exceptions import BadRequestException, NotFoundException
from app.schemas.task import TaskCreate


# TASK CRUD


async def create_task(
    db: AsyncSession,
    task_in: TaskCreate,
) -> Task:
    """Create a new task"""

    task = Task(
        title=task_in.title,
        project_id=task_in.project_id,
        type_id=task_in.type_id,
        status=TaskStatusEnum.PENDING,
        priority=task_in.priority,
    )

    db.add(task)

    try:
        await db.commit()
    except IntegrityError as exc:
        await db.rollback()
        raise BadRequestException("Invalid project, type, or priority value") from exc

    await db.refresh(task)
    return task


async def get_task_by_id(
    db: AsyncSession,
    task_id: int,
) -> Task:
    """Fetch a task by its ID"""

    result = await db.execute(select(Task).where(Task.id == task_id))
    task = result.scalar_one_or_none()

    if not task:
        raise NotFoundException("Task not found")

    return task


async def get_tasks_by_project(
    db: AsyncSession,
    project_id: int,
) -> list[Task]:
    """Fetch all tasks belonging to a project"""

    result = await db.execute(select(Task).where(Task.project_id == project_id))
    return result.scalars().all()


async def get_all_tasks(db: AsyncSession) -> list[Task]:
    """Fetch all tasks"""

    result = await db.execute(select(Task))
    return result.scalars().all()


async def update_task_status(
    db: AsyncSession,
    task_id: int,
    status: TaskStatusEnum,
) -> Task:
    """Update only the status of a task"""

    result = await db.execute(select(Task).where(Task.id == task_id))
    task = result.scalar_one_or_none()

    if not task:
        raise NotFoundException("Task not found")

    task.status = status

    try:
        await db.commit()
    except IntegrityError as exc:
        await db.rollback()
        raise BadRequestException("Invalid status value") from exc

    await db.refresh(task)
    return task


# TASK TYPE CRUD


async def get_all_task_types(
    db: AsyncSession,
) -> list[TaskType]:
    """Return all task types"""

    result = await db.execute(select(TaskType).order_by(TaskType.id))
    return result.scalars().all()
