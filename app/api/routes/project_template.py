from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.crud.project_template import get_all_project_templates
from app.schemas.project_template import ProjectTemplateOut

router = APIRouter(
    prefix="/project/templates",
    tags=["Project Templates"],
)

@router.get("/", response_model=list[ProjectTemplateOut])
def list_project_templates(db: Session = Depends(get_db)):
    """Retrieve all project templates"""
    return get_all_project_templates(db)
