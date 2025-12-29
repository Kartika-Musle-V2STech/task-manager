from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.core.database import Base


class ProjectMember(Base):
    """
    Association table representing users participating in a project
    with a specific role.
    """

    __tablename__ = "project_members"

    __table_args__ = (
        UniqueConstraint("user_id", "project_id", name="uq_user_project"),
    )

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    project_id = Column(
        Integer,
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    role_id = Column(
        Integer,
        ForeignKey("roles.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    # Relationships
    user = relationship("User", back_populates="project_members")
    project = relationship("Project", back_populates="members")
    role = relationship(
        "Role",
        back_populates="project_members",
        foreign_keys=[role_id],
    )
