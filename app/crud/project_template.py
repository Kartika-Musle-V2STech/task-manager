from sqlalchemy.orm import Session
from app.models.project_template import ProjectTemplate

"""
Return all project templates
"""
def get_all_project_templates(db: Session):
    return db.query(ProjectTemplate).order_by(ProjectTemplate.id).all()
    