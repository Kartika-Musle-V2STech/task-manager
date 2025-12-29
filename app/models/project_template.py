from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.core.database import Base


class ProjectTemplate(Base):
    """
    Blueprint for creating projects.
    Defines project types.
    """

    __tablename__ = "project_templates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text, nullable=False)

    projects = relationship(
        "Project",
        back_populates="project_template"
    )
