"""
API dependencies.
"""

from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import AsyncSessionLocal


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Provide an async database session to API routes.
    """
    async with AsyncSessionLocal() as db:
        yield db
