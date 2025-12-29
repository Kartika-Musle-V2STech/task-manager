from pydantic import BaseModel, EmailStr, Field, ConfigDict, field_validator

class UserBase(BaseModel):
    name: str
    email: EmailStr
    role_id: int

class UserCreate(UserBase):
    password: str = Field(
        min_length=4,
        max_length=72,
        description="Password must be between 4 and 128 characters"
    )

class UserOut(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)