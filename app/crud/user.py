from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password

def create_user(db: Session, user_in: UserCreate) -> User:
    """Creates a new user
    This function hashes the provided password
    """
    try:
        hashed_pw = hash_password(user_in.password)
    except Exception as e:
        raise ValueError(f"Password hashing failed: {str(e)}")
    
    user = User(
        name=user_in.name,
        email=user_in.email,
        password_hash=hashed_pw,
        role_id=user_in.role_id  
    )

    db.add(user)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("User with this email already exists")

    db.refresh(user)
    return user


def get_all_users(db: Session) -> list[User]:
    """Retrive all users from the database
    Returns a list of all users ordered by their ID
    """
    return db.query(User).order_by(User.id).all()


def get_user_by_id(db: Session, user_id: int) -> User | None:
    """
    Retrieve a single user by their unique ID
    Returns None if the user does not exist
    """
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> User | None:
    """
    Retrieve a single user by their email address
    Returns None if no matching user is found
    """
    return db.query(User).filter(User.email == email).first()