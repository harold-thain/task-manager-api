from sqlalchemy import Column, Integer, String, Date, Enum as SQLEnum
from app.database import Base
import enum


class TaskStatus(str, enum.Enum):
    pending = "pending"
    completed = "completed"


class Task(Base):
    """
    This class maps directly to a 'tasks' table in the database.
    Each attribute = a column.
    """
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(String(1000), nullable=True)
    due_date = Column(Date, nullable=True)
    status = Column(SQLEnum(TaskStatus), default=TaskStatus.pending)