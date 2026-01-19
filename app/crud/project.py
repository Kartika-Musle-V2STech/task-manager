"""
CRUD operations for Projects, Project Templates, and Project Members (Async).
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import IntegrityError

from app.core.models import Project, ProjectTemplate, ProjectMember
from app.core.exceptions import BadRequestException, NotFoundException
from app.schemas.project import ProjectCreate, ProjectMemberCreate


# PROJECT CRUD


async def create_project(
    db: AsyncSession,
    project_in: ProjectCreate,
) -> Project:
    """
    Create a new project.
    Project is created from a project template and associated with a creator user.
    """

    project = Project(
        project_template_id=project_in.project_template_id,
        start_date=project_in.start_date,
        end_date=project_in.end_date,
        created_by_id=project_in.created_by_id,
    )

    db.add(project)

    try:
        await db.commit()
    except IntegrityError as exc:
        await db.rollback()
        raise BadRequestException("Invalid Project or Duplicate Project") from exc

    await db.refresh(project)

    result = await db.execute(
        select(Project)
        .options(
            selectinload(Project.created_by),  # Changed from joinedload
            selectinload(Project.project_template),  # Changed from joinedload
        )
        .where(Project.id == project.id)
    )

    return result.scalar_one()


async def get_all_projects(db: AsyncSession) -> list[Project]:
    """Retrieve all projects"""

    result = await db.execute(
        select(Project)
        .options(
            selectinload(Project.created_by),
            selectinload(Project.project_template),
        )
        .order_by(Project.id)
    )

    return result.scalars().all()


# PROJECT TEMPLATE CRUD


async def get_all_project_templates(
    db: AsyncSession,
) -> list[ProjectTemplate]:
    """Return all project templates"""

    result = await db.execute(select(ProjectTemplate).order_by(ProjectTemplate.id))

    return result.scalars().all()


# PROJECT MEMBER CRUD


async def add_project_member(
    db: AsyncSession,
    member_in: ProjectMemberCreate,
) -> ProjectMember:
    """Add a user to a project with a role"""

    member = ProjectMember(
        user_id=member_in.user_id,
        project_id=member_in.project_id,
        role_id=member_in.role_id,
    )

    db.add(member)

    try:
        await db.commit()
    except IntegrityError as exc:
        await db.rollback()
        raise BadRequestException(
            "User already assigned to this project or invalid IDs"
        ) from exc

    await db.refresh(member)

    result = await db.execute(
        select(ProjectMember)
        .options(
            selectinload(ProjectMember.user),
            selectinload(ProjectMember.project),
            selectinload(ProjectMember.role),
        )
        .where(ProjectMember.id == member.id)
    )

    return result.scalar_one()


async def get_project_members(
    db: AsyncSession,
    project_id: int,
) -> list[ProjectMember]:
    """Retrieve all members of a project"""

    result = await db.execute(
        select(ProjectMember)
        .options(
            selectinload(ProjectMember.user),
            selectinload(ProjectMember.project),
            selectinload(ProjectMember.role),
        )
        .where(ProjectMember.project_id == project_id)
    )

    members = result.scalars().all()

    if not members:
        raise NotFoundException("No members found for this project")

    return members
