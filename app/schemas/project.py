"""
Schemas for Project, Project Template, and Project Member operations.
"""

from datetime import date
from pydantic import BaseModel, ConfigDict

# SHARED / BASIC SCHEMAS


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
    end_date: date | None

    model_config = ConfigDict(from_attributes=True)


class ProjectTemplateBasicInfo(BaseModel):
    """Basic project template information"""

    id: int
    name: str
    description: str

    model_config = ConfigDict(from_attributes=True)


# PROJECT SCHEMAS


class ProjectCreate(BaseModel):
    """Schema used when creating a new project"""

    project_template_id: int
    start_date: date
    end_date: date | None = None
    created_by_id: int


class ProjectOut(BaseModel):
    """Schema returned when a project is fetched or created"""

    project_template_id: int
    start_date: date
    end_date: date | None
    created_by_id: int

    created_by: UserBasicInfo
    project_template: ProjectTemplateBasicInfo

    model_config = ConfigDict(from_attributes=True)


# PROJECT TEMPLATE SCHEMAS


class ProjectTemplateBase(BaseModel):
    """Base schema for project templates"""

    name: str
    description: str | None = None


class ProjectTemplateCreate(ProjectTemplateBase):
    """Schema used when creating a project template"""


class ProjectTemplateOut(ProjectTemplateBase):
    """Schema returned when a project template is fetched or listed"""

    id: int

    model_config = ConfigDict(from_attributes=True)


# PROJECT MEMBER SCHEMAS


class ProjectMemberCreate(BaseModel):
    """Schema used when assigning a user to a project"""

    user_id: int
    project_id: int
    role_id: int


class ProjectMemberOut(BaseModel):
    """
    Schema returned when a project member assignment is created or fetched
    """

    id: int
    user_id: int
    project_id: int
    role_id: int

    user: UserBasicInfo
    project: ProjectBasicInfo
    role: RoleBasicInfo

    model_config = ConfigDict(from_attributes=True)
