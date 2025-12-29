from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.crud.role import get_all_roles
from app.schemas.role import RoleOut

router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)

@router.get("/", response_model=list[RoleOut])
def list_roles(db: Session = Depends(get_db)):
    return get_all_roles(db)