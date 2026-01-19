"""
This module contains the database initialization function.
It creates all tables defined in the SQLAlchemy Base metadata.
"""

from app.core.database import engine, Base


async def init_db():
    """Initialize the database by creating all tables."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
