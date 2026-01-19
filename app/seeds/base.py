"""
Base seeding utilities (Async).
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError


async def get_or_create(db: AsyncSession, model, defaults=None, **filters):
    stmt = select(model).filter_by(**filters)
    result = await db.execute(stmt)
    instance = result.scalars().first()

    if instance:
        return instance

    params = dict(filters)
    if defaults:
        params.update(defaults)

    instance = model(**params)
    db.add(instance)

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        result = await db.execute(stmt)
        return result.scalars().first()

    await db.refresh(instance)
    return instance
