from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.crud.project import create_project, get_all_projects
from app.schemas.project import ProjectCreate, ProjectOut

router = APIRouter(
    prefix="/projects",
    tags=['Projects']
)

@router.get("/", response_model=list[ProjectOut])
def list_projects(db: Session = Depends(get_db)):
    return get_all_projects(db)

@router.post("/", response_model=ProjectOut)
def create_new_project(
    project_in: ProjectCreate,
    db: Session = Depends(get_db),
):
    try: 
        return create_project(db, project_in)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
