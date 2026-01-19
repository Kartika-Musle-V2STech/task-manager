"""
User CRUD operations (Async).
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.core.models import User
from app.core.exceptions import BadRequestException, NotFoundException
from app.core.security import hash_password
from app.schemas.user import UserCreate


# USER CRUD


async def create_user(
    db: AsyncSession,
    user_in: UserCreate,
) -> User:
    """Create a new user and hash the password"""

    hashed_pw = hash_password(user_in.password)

    user = User(
        name=user_in.name,
        email=user_in.email,
        password_hash=hashed_pw,
        role_id=user_in.role_id,
    )

    db.add(user)

    try:
        await db.commit()
    except IntegrityError as exc:
        await db.rollback()
        raise BadRequestException("User with this email already exists") from exc

    await db.refresh(user)
    return user


async def get_all_users(db: AsyncSession) -> list[User]:
    """Retrieve all users ordered by ID"""

    result = await db.execute(select(User).order_by(User.id))
    return result.scalars().all()


async def get_user_by_id(
    db: AsyncSession,
    user_id: int,
) -> User:
    """Retrieve a single user by ID"""

    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalars().first()

    if not user:
        raise NotFoundException("User not found")

    return user


async def get_user_by_email(
    db: AsyncSession,
    email: str,
) -> User:
    """Retrieve a single user by email"""

    result = await db.execute(select(User).filter(User.email == email))
    user = result.scalars().first()

    if not user:
        raise NotFoundException("User not found")

    return user
