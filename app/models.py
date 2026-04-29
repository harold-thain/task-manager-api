from pydantic import BaseModel
from typing import Optional
from datetime import date
from enum import Enum


class TaskStatus(str, Enum):
    pending = "pending"
    completed = "completed"


class TaskCreate(BaseModel):
    """The shape of data we EXPECT when someone creates a task."""
    title: str
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: TaskStatus = TaskStatus.pending


class TaskResponse(BaseModel):
    """The shape of data we SEND BACK in responses."""
    id: int
    title: str
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: TaskStatus