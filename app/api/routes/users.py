"""
API routes for User operations.
"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.crud.user import create_user, get_all_users
from app.schemas.user import UserCreate, UserOut

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get(
    "/",
    response_model=list[UserOut],
    summary="List users",
)
async def list_users(db: AsyncSession = Depends(get_db)):
    """Retrieve all users"""
    return await get_all_users(db)


@router.post(
    "/",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
    summary="Create user",
)
async def create_new_user(
    user_in: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    """Create a new user"""
    return await create_user(db, user_in)
