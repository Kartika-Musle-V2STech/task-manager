"""
Module to seed task description data.
"""

from sqlalchemy.ext.asyncio import AsyncSession
from app.core.models import TaskType
from app.seeds.base import get_or_create


async def seed_task_data(db: AsyncSession):
    """
    Seed task-related master data.
    - TaskStatus and TaskPriority are ENUMs and MUST NOT be seeded.
    - Only TaskType is stored as a table and seeded here.
    """

    task_types = [
        "New Feature",
        "Change Request",
        "Bug Fixing",
        "Testing",
        "Deployment",
        "Other",
    ]

    for task_type in task_types:
        await get_or_create(db, TaskType, name=task_type)
