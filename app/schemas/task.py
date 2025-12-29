from pydantic import BaseModel, ConfigDict
from app.models.enum import TaskStatusEnum, TaskPriorityEnum

class TaskBase(BaseModel):
    """Base Schema containing common fields shared by all task related schemas"""
    title: str
    project_id: int
    type_id: int
    status: TaskStatusEnum
    priority: TaskPriorityEnum

class TaskCreate(TaskBase):
    """
    schema used when creating a new task"""
    pass

class TaskOut(TaskBase):
    """Schema returned in API response when a task is fetches"""
    id: int
    
    model_config = ConfigDict(from_attributes=True)

class TaskStatusUpdate(BaseModel):
    """Schema used to update the status of an existing task"""
    status: TaskStatusEnum
