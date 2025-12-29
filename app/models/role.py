from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Role(Base):
    """
    Represents a role. Used for users and project memberships
    """

    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)

    #Relationship
    users = relationship("User", back_populates="role")
    project_members = relationship("ProjectMember", back_populates="role", foreign_keys="ProjectMember.role_id", cascade="all, delete-orphan")

    