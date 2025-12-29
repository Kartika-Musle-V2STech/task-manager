from pydantic import BaseModel, ConfigDict
from datetime import date  # Add this import

class ProjectMemberCreate(BaseModel):
    """
    Schema used when assigning a user to a project
    """
    user_id: int
    project_id: int
    role_id: int

class UserBasicInfo(BaseModel):
    """Basic user information for nested display"""
    id: int
    name: str
    email: str
    
    model_config = ConfigDict(from_attributes=True)

class RoleBasicInfo(BaseModel):
    """Basic role information for nested display"""
    id: int
    name: str
    
    model_config = ConfigDict(from_attributes=True)

class ProjectBasicInfo(BaseModel):
    """Basic project information for nested display"""
    id: int
    project_template_id: int
    start_date: date  
    end_date: date    
    
    model_config = ConfigDict(from_attributes=True)

class ProjectMemberOut(BaseModel):
    """
    Schema returned in API responses when a project member assignment is created or fetched
    Includes related user, project, and role information
    """
    id: int
    user_id: int
    project_id: int
    role_id: int
    
    # Nested relationships
    user: UserBasicInfo
    project: ProjectBasicInfo
    role: RoleBasicInfo

    model_config = ConfigDict(from_attributes=True)