from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import IntegrityError

from app.models.project_member import ProjectMember
from app.schemas.project_member import ProjectMemberCreate

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
    except IntegrityError:
        db.rollback()
        raise ValueError("User already assigned to this project or invalid IDs")

    db.refresh(member)
    
    # Reload with relationships
    return db.query(ProjectMember).options(
        joinedload(ProjectMember.user),
        joinedload(ProjectMember.project),
        joinedload(ProjectMember.role)
    ).filter(ProjectMember.id == member.id).first()


def get_project_members(db: Session, project_id: int) -> list[ProjectMember]:
    """Get all members of a project with related user, project, and role data"""
    return (
        db.query(ProjectMember)
        .options(
            joinedload(ProjectMember.user),
            joinedload(ProjectMember.project),
            joinedload(ProjectMember.role)
        )
        .filter(ProjectMember.project_id == project_id)
        .all()
    )