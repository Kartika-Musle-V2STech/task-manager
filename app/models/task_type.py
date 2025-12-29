from sqlalchemy.sql._typing import Nullable
from sqlalchemy import Column, Integer, String
from app.core.database import Base

class TaskType(Base):
    """
    Task Category Table
    """
    __tablename__ = "task_type"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)

    