from sqlalchemy import null
from enum import Enum as PyEnum
from datetime import date

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Date,
    Text,
    Enum,
    UniqueConstraint,
)

from sqlalchemy.orm import relationship
from app.core.database import Base


# Enum
class TaskStatusEnum(str, PyEnum):
    """Enum Class"""

    PENDING = "pending"
    ONGOING = "ongoing"
    COMPLETED = "completed"
    CANCELLED = "cancalled"

    @classmethod
    def values(cls) -> list[str]:
        return [e.value for e in cls]


class TaskPriorityEnum(str, PyEnum):
    """Task Priority Enum Class"""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

    @classmethod
    def values(cls) -> list[str]:
        """Returns a list of all values in the enum."""
        return [e.value for e in cls]


# Role


class Role(Base):
    """Represents a role. Used for users and project members"""

    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)

    users = relationship("User", back_populates="role")
    project_members = relationship(
        "ProjectMember",
        back_populates="role",
        cascade="all, delete-orphan",
    )


# User


class User(Base):
    """Represents a user"""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True, index=True)
    password_hash = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)

    role_id = Column(
        Integer, ForeignKey("roles.id", ondelete="RESTRICT"), nullable=False
    )

    role = relationship("Role", back_populates="users")
    project_members = relationship(
        "ProjectMember",
        back_populates="user",
        cascade="all, delete-orphan",
    )
    task_assignments = relationship(
        "UserTaskHistory",
        back_populates="user",
        cascade="all, delete-orphan",
    )
    created_projects = relationship("Project", back_populates="created_by")


# Project Template


class ProjectTemplate(Base):
    """Blueprint for creating projects"""

    __tablename__ = "project_templates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text, nullable=False)

    projects = relationship("Project", back_populates="project_template")


# Project


class Project(Base):
    """Represent an active project created from a project template"""

    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)

    project_template_id = Column(
        Integer,
        ForeignKey("project_templates.id", ondelete="RESTRICT"),
        index=True,
    )

    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)

    created_by_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    project_template = relationship("ProjectTemplate", back_populates="projects")
    created_by = relationship("User", back_populates="created_projects")
    members = relationship(
        "ProjectMember",
        back_populates="project",
        cascade="all, delete-orphan",
    )
    tasks = relationship(
        "Task",
        back_populates="project",
        cascade="all, delete-orphan",
    )


# Project Member


class ProjectMember(Base):
    """
    Association table representing users participating in a project
    with a specific role.
    """

    __tablename__ = "project_members"
    __table_args__ = (
        UniqueConstraint("user_id", "project_id", name="uq_user_project"),
    )

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    project_id = Column(
        Integer,
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    role_id = Column(
        Integer,
        ForeignKey("roles.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    user = relationship("User", back_populates="project_members")
    project = relationship("Project", back_populates="members")
    role = relationship("Role", back_populates="project_members")


# Task Type


class TaskType(Base):
    """
    Task category table
    """

    __tablename__ = "task_type"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)


# Task


class Task(Base):
    """
    Represents a task within a project
    """

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)

    project_id = Column(
        Integer,
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False,
    )
    type_id = Column(
        Integer,
        ForeignKey("task_type.id", ondelete="RESTRICT"),
        nullable=False,
    )

    status = Column(
        Enum(
            TaskStatusEnum,
            name="task_status_enum",
            values_callable=lambda x: x.values(),
        ),
        nullable=False,
        index=True,
    )

    priority = Column(
        Enum(
            TaskPriorityEnum,
            name="task_priority_enum",
            values_callable=lambda x: x.values(),
        ),
        nullable=False,
        index=True,
    )

    project = relationship("Project", back_populates="tasks")
    task_type = relationship("TaskType")
    assignments = relationship(
        "UserTaskHistory",
        back_populates="task",
        cascade="all, delete-orphan",
    )


# User Task History


class UserTaskHistory(Base):
    """
    Tracks user-task assignments over time.
    """

    __tablename__ = "user_task_history"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )
    task_id = Column(
        Integer,
        ForeignKey("tasks.id", ondelete="CASCADE"),
        nullable=False,
    )
    role_id = Column(
        Integer,
        ForeignKey("roles.id", ondelete="RESTRICT"),
        nullable=False,
    )

    user = relationship("User", back_populates="task_assignments")
    task = relationship("Task", back_populates="assignments")
    role = relationship("Role")
