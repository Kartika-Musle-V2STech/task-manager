"""
This module defines the lifespan context manager for the FastAPI application.
It handles startup and shutdown events, such as creating database tables.
"""

from contextlib import asynccontextmanager

from app.core.database import engine
from app.core.models import Base


@asynccontextmanager
async def lifespan(app):
    print("Application starting")

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    print("Application shutdown")
