from logging.config import fileConfig

from alembic import context
from sqlalchemy import pool

from app.core.database import engine, Base

# Import all models so Alembic can detect them
from app.models.user import User
from app.models.role import Role
from app.models.project import Project
from app.models.project_template import ProjectTemplate
from app.models.project_member import ProjectMember
from app.models.task import Task
from app.models.task_type import TaskType
from app.models.history import UserTaskHistory


# Alembic Config object
config = context.config

# Configure logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set target metadata for autogenerate
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """
    Run migrations in offline mode.
    """
    context.configure(
        url=str(engine.url),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """
    Run migrations in online mode.
    """
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
