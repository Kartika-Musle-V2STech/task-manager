from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.crud.project_member import add_project_member, get_project_members
from app.schemas.project_member import ProjectMemberCreate, ProjectMemberOut

router = APIRouter(
    prefix="/project/members",
    tags=["Project Members"]
)

@router.post("/", response_model=ProjectMemberOut)
def add_member(
    member_in: ProjectMemberCreate,
    db: Session=Depends(get_db),
):
    """Assign a user to a project with a specific role"""
    try:
        return add_project_member(db, member_in)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get(
    "/project/{project_id}",
    response_model=list[ProjectMemberOut]
)
def list_project_members(
    project_id: int,
    db: Session = Depends(get_db),
):
    """Retrieve all members assigned to a project"""
    return get_project_members(db, project_id)