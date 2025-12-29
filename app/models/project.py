from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Project(Base):
    """
    Represents active project created from project template
    Project is based on project template
    has start date and end date
    can have multiple members
    can have multiple tasks
    """
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    project_template_id = Column(
        Integer,
        ForeignKey("project_templates.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)

    created_by_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relationships
    project_template = relationship("ProjectTemplate", back_populates="projects")
    created_by = relationship("User", back_populates="created_projects")
    members = relationship("ProjectMember", back_populates="project", cascade="all, delete-orphan")
    tasks = relationship("Task", back_populates="project", cascade="all, delete-orphan")
