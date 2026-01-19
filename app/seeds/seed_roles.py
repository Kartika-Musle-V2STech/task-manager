"""
Module for seeding role data into the database.
"""
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models import Role
from app.seeds.base import get_or_create


async def seed_roles(db: AsyncSession):
    """
    Seed for job roles. Used for user profile and project/task context
    """
    roles = [
        "Software Engineer",
        "AI Engineer",
        "Data Engineer",
        "Data Scientist",
        "DevOps Engineer",
        "Full Stack Engineer",
        "Frontend Engineer",
        "Java Developer",
        "Mobile Engineer",
        "QA Engineer",
    ]

    for role in roles:
        await get_or_create(db, Role, name=role)
