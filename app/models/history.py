from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base

class UserTaskHistory(Base):
    """
    Association table that tracks user-task assignments over time.
    Represents which user was assigned to which task with which role
    """
    __tablename__ = "user_task_history"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    task_id = Column(Integer, ForeignKey("tasks.id", ondelete="CASCADE"), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id", ondelete="RESTRICT"), nullable=False)
    
    #Relationship

    user = relationship("User", back_populates="task_assignments")
    task = relationship("Task", back_populates="assignments")
    role = relationship("Role")



    