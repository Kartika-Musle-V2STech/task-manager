"""
This module imports all SQLAlchemy model classes.
SQLAlchemy only registers models that are imported.
Importing all models here ensures table creation,
relationship resolution, and migration generation work correctly.
"""

from app.models.user import User
from app.models.role import Role
from app.models.project_template import ProjectTemplate
from app.models.project import Project
from app.models.project_member import ProjectMember
from app.models.task_type import TaskType
from app.models.task import Task
from app.models.history import UserTaskHistory

