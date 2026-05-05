from sqlalchemy import Column, Integer, String, Date, Enum as SQLEnum, ForeignKey
from sqlalchemy.orm import relationship
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
    
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Placeholder for future user association
    
    owner = relationship("User", back_populates="tasks")  # Placeholder for future user association
    
    
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    
    tasks = relationship("Task", back_populates="user")