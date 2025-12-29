from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import IntegrityError
from app.models.project import Project
from app.schemas.project import ProjectCreate

def create_project(db: Session, project_in: ProjectCreate) -> Project:
    """Create a new project. 
    Project is created from a project template and associated with a creator user
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
    except IntegrityError:
        db.rollback()
        raise ValueError("Invalid Project or Duplicate Project")

    db.refresh(project)
    return db.query(Project).options(
        joinedload(Project.created_by),
        joinedload(Project.project_template)
    ).filter(Project.id == project.id).first()

def get_all_projects(db:Session) -> list[Project]:
    """Retrieve all projects"""
    return (
        db.query(Project)
        .options(
            joinedload(Project.created_by),
            joinedload(Project.project_template)
        )
        .order_by(Project.id)
        .all()
    )