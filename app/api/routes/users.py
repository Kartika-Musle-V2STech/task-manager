from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.crud.user import create_user, get_all_users
from app.schemas.user import UserCreate, UserOut

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/", response_model=UserOut)
def create_new_user(
    user_in: UserCreate,
    db: Session = Depends(get_db),
):
    """Create a new user"""
    try:
        return create_user(db, user_in)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[UserOut])
def list_users(db: Session = Depends(get_db)):
    """Retrieve all users"""
    return get_all_users(db)
