"""
CRUD operations for Role model.
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.models import Role


async def get_all_roles(db: AsyncSession) -> list[Role]:
    """Return all roles"""
    result = await db.execute(select(Role).order_by(Role.id))
    return result.scalars().all()
