from pydantic import BaseModel
from typing import Optional
from datetime import date
from app.models import TaskStatus


class TaskCreate(BaseModel):
    """What we expect the client to send when creating/updating a task."""
    title: str
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: TaskStatus = TaskStatus.pending


class TaskResponse(BaseModel):
    """What we send back in responses."""
    id: int
    title: str
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: TaskStatus

    class Config:
        from_attributes = True  # lets Pydantic read SQLAlchemy objects directly