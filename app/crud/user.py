"""
User CRUD operations.
"""

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.core.models import User
from app.core.exceptions import BadRequestException, NotFoundException
from app.core.security import hash_password
from app.schemas.user import UserCreate


def create_user(db: Session, user_in: UserCreate) -> User:
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
        db.commit()
    except IntegrityError:
        db.rollback()
        raise BadRequestException("User with this email already exists")

    db.refresh(user)
    return user


def get_all_users(db: Session) -> list[User]:
    """Retrieve all users ordered by ID"""
    return db.query(User).order_by(User.id).all()


def get_user_by_id(db: Session, user_id: int) -> User:
    """Retrieve a single user by ID"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise NotFoundException("User not found")
    return user


def get_user_by_email(db: Session, email: str) -> User:
    """Retrieve a single user by email"""
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise NotFoundException("User not found")
    return user
