from pydantic import BaseModel, EmailStr, Field, ConfigDict, field_validator


class UserBase(BaseModel):
    """
    Base schema for user data.
    """

    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    role_id: int = Field(..., gt=0)


class UserCreate(UserBase):
    """
    Schema for creating a new user with a password.
    """

    password: str = Field(
        min_length=4,
        max_length=72,
        description="Password must be between 4 and 128 characters",
    )


class UserOut(UserBase):
    """
    Schema for user output response.
    """

    id: int
    model_config = ConfigDict(from_attributes=True)
