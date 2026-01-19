"""
API routes for Role management.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.crud.role import get_all_roles
from app.schemas.role import RoleOut

router = APIRouter(
    prefix="/roles",
    tags=["Roles"],
)


@router.get(
    "/",
    response_model=list[RoleOut],
    summary="List roles",
)
async def list_roles(db: AsyncSession = Depends(get_db)):
    """Retrieve all available roles"""
    return await get_all_roles(db)
