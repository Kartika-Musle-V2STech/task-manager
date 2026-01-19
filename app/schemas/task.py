"""
Module for Task Pydantic schemas.
"""

from pydantic import Field, BaseModel, ConfigDict
from app.core.models import TaskStatusEnum, TaskPriorityEnum

# TASK SCHEMAS


class TaskBase(BaseModel):
    """Fields common to task creation and output"""

    title: str = Field(..., min_length=3, max_length=50)
    project_id: int = Field(..., gt=0)
    type_id: int = Field(..., gt=0)
    priority: TaskPriorityEnum


class TaskCreate(TaskBase):
    """Schema used when creating a new task"""

    # status should NOT be client-controlled at creation


class TaskOut(BaseModel):
    """Schema returned in API response when a task is fetched"""

    id: int
    title: str
    project_id: int
    type_id: int
    status: TaskStatusEnum
    priority: TaskPriorityEnum

    model_config = ConfigDict(from_attributes=True)


class TaskStatusUpdate(BaseModel):
    """Schema used to update the status of an existing task"""

    status: TaskStatusEnum


# TASK TYPE SCHEMA


class TaskTypeOut(BaseModel):
    """Schema returned in API responses when task types are fetched or listed"""

    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)
