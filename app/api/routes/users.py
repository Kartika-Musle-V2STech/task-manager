"""
API routes for User operations.
"""

from fastapi import APIRouter, Depends, status  # 🔁 CHANGED
from sqlalchemy.orm import Session

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
def list_users(db: Session = Depends(get_db)):
    """Retrieve all users"""
    return get_all_users(db)


@router.post(
    "/",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
    summary="Create user",
)
def create_new_user(
    user_in: UserCreate,
    db: Session = Depends(get_db),
):
    """Create a new user"""
    return create_user(db, user_in)  
