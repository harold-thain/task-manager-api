from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date
from app.models import TaskStatus


# --- User Schemas ---

class UserCreate(BaseModel):
    """What we expect when someone registers."""
    name: str
    email: EmailStr   # Pydantic validates this is a real email format
    password: str


class UserResponse(BaseModel):
    """What we send back — notice password is NOT here."""
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


# --- Task Schemas (unchanged) ---

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: TaskStatus = TaskStatus.pending


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: TaskStatus

    class Config:
        from_attributes = True