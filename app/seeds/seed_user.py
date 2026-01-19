"""Seed data for users."""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.models import User, Role
from app.seeds.base import get_or_create


async def seed_system_users(db: AsyncSession):
    """
    Seed system/demo users used for project creation and history tracking
    """

    result = await db.execute(select(Role).order_by(Role.id))
    default_role = result.scalar_one_or_none()

    if not default_role:
        raise RuntimeError("Roles must be seeded before users")

    users = [
        {
            "email": "system@app.local",
            "name": "System",
        },
        {
            "email": "admin@app.local",
            "name": "Admin Bot",
        },
    ]

    for u in users:
        await get_or_create(
            db,
            User,
            email=u["email"],
            defaults={
                "name": u["name"],
                "password_hash": "SYSTEM_USER",
                "role_id": default_role.id,
            },
        )
