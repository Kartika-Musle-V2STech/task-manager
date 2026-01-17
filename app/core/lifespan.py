"""
Lifespan events handler for the application.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handle the application lifespan (startup and shutdown)
    """
    print("Application Starting")

    yield

    print("Application shutting down")
