from pydantic import BaseModel, ConfigDict

class RoleBase(BaseModel):
    """Base schema containing fields common to all role-related schemas"""
    name: str

class RoleCreate(RoleBase):
    """Schema used when creating a new role"""
    pass

class RoleOut(RoleBase):
    """Schema returned in API responses when a role is fetched or listed"""
    id: int

    model_config = ConfigDict(from_attributes=True)