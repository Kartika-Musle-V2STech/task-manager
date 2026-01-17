"""
CRUD operations for Projects, Project Templates, and Project Members.
"""

from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import IntegrityError

from app.core.models import Project, ProjectTemplate, ProjectMember
from app.core.exceptions import BadRequestException, NotFoundException
from app.schemas.project import ProjectCreate, ProjectMemberCreate


# PROJECT CRUD


def create_project(db: Session, project_in: ProjectCreate) -> Project:
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
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise BadRequestException("Invalid Project or Duplicate Project") from exc

    db.refresh(project)

    return (
        db.query(Project)
        .options(
            joinedload(Project.created_by),
            joinedload(Project.project_template),
        )
        .filter(Project.id == project.id)
        .first()
    )


def get_all_projects(db: Session) -> list[Project]:
    """Retrieve all projects"""
    return (
        db.query(Project)
        .options(
            joinedload(Project.created_by),
            joinedload(Project.project_template),
        )
        .order_by(Project.id)
        .all()
    )


# PROJECT TEMPLATE CRUD


def get_all_project_templates(db: Session) -> list[ProjectTemplate]:
    """Return all project templates"""
    return db.query(ProjectTemplate).order_by(ProjectTemplate.id).all()


# PROJECT MEMBER CRUD


def add_project_member(db: Session, member_in: ProjectMemberCreate) -> ProjectMember:
    """Add a user to a project with a role"""
    member = ProjectMember(
        user_id=member_in.user_id,
        project_id=member_in.project_id,
        role_id=member_in.role_id,
    )

    db.add(member)

    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise BadRequestException(
            "User already assigned to this project or invalid IDs"
        ) from exc

    db.refresh(member)

    return (
        db.query(ProjectMember)
        .options(
            joinedload(ProjectMember.user),
            joinedload(ProjectMember.project),
            joinedload(ProjectMember.role),
        )
        .filter(ProjectMember.id == member.id)
        .first()
    )


def get_project_members(db: Session, project_id: int) -> list[ProjectMember]:
    """Retrieve all members of a project"""
    members = (
        db.query(ProjectMember)
        .options(
            joinedload(ProjectMember.user),
            joinedload(ProjectMember.project),
            joinedload(ProjectMember.role),
        )
        .filter(ProjectMember.project_id == project_id)
        .all()
    )

    if not members:
        raise NotFoundException("No members found for this project")

    return members
