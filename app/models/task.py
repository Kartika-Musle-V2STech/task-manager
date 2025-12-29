from app.models.enum import TaskStatusEnum, TaskPriorityEnum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.core.database import Base

class Task(Base):
    """
    Represents a task within a project
    task belongs to a single project
    has predefined type, status, priority
    can be assigned to one or more users via UserTaskHistory
    """

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    type_id = Column(Integer, ForeignKey("task_type.id", ondelete="RESTRICT"), nullable=False)
    status = Column(Enum(TaskStatusEnum, name="task_status_enum",values_callable=lambda enum_cls: enum_cls.values()),nullable=False, index=True)
    priority = Column(Enum(TaskPriorityEnum, name="task_priority_enum",values_callable=lambda enum_cls: enum_cls.values()), nullable=False, index=True)

    #Relationship
    project = relationship("Project", back_populates="tasks")
    task_type = relationship("TaskType")

    assignments = relationship("UserTaskHistory", back_populates="task", cascade="all, delete-orphan")
