from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.crud.task_type import get_all_task_types
from app.schemas.task_type import TaskTypeOut

router = APIRouter(
    prefix="/task/types",
    tags=["Task Types"],
)

@router.get("/", response_model = list[TaskTypeOut])
def list_task_types(db: Session = Depends(get_db)):
    """Retrieve all task types"""
    return get_all_task_types(db)