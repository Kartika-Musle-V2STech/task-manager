"""
API routes for Project Setup:
- Projects
- Project Templates
- Project Members
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.crud.project import (
    create_project,
    get_all_projects,
    get_all_project_templates,
    add_project_member,
    get_project_members,
)
from app.schemas.project import (
    ProjectCreate,
    ProjectOut,
    ProjectTemplateOut,
    ProjectMemberCreate,
    ProjectMemberOut,
)

router = APIRouter(
    prefix="/projects",
    tags=["Project Setup"],
)

# PROJECTS


@router.get(
    "/",
    response_model=list[ProjectOut],
    summary="List projects",
)
def list_projects(db: Session = Depends(get_db)):
    """Retrieve a list of all projects"""
    return get_all_projects(db)


@router.post(
    "/",
    response_model=ProjectOut,
    summary="Create project",
)
def create_new_project(
    project_in: ProjectCreate,
    db: Session = Depends(get_db),
):
    """Create a new project"""
    return create_project(db, project_in)


# PROJECT TEMPLATES


@router.get(
    "/templates",
    response_model=list[ProjectTemplateOut],
    summary="List project templates",
)
def list_project_templates(db: Session = Depends(get_db)):
    """Retrieve all project templates"""
    return get_all_project_templates(db)


# PROJECT MEMBERS


@router.post(
    "/members",
    response_model=ProjectMemberOut,
    summary="Add project member",
)
def add_member(
    member_in: ProjectMemberCreate,
    db: Session = Depends(get_db),
):
    """Assign a user to a project with a specific role"""
    return add_project_member(db, member_in)


@router.get(
    "/{project_id}/members",
    response_model=list[ProjectMemberOut],
    summary="List project members",
)
def list_project_members(
    project_id: int,
    db: Session = Depends(get_db),
):
    """Retrieve all members assigned to a project"""
    return get_project_members(db, project_id)
