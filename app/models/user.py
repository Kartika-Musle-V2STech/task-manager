from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class User(Base):
    """
    Represents a user. 
    User can belong to one role, or be assigned to multiple tasks, multiple projects

    User table stores authentication and user information only
    """

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True, index=True)
    password_hash = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)

    role_id = Column(Integer, ForeignKey("roles.id", ondelete="RESTRICT"), nullable=False)
    
    #Relationship
    role = relationship("Role", back_populates="users")
    project_members = relationship("ProjectMember", back_populates="user", cascade="all, delete-orphan")
    task_assignments = relationship("UserTaskHistory", back_populates="user", cascade="all, delete-orphan")
    created_projects = relationship("Project", back_populates="created_by")