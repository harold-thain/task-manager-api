from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date
from app.models import TaskStatus


# --- User Schemas ---

class UserCreate(BaseModel):
    """What we expect when someone registers."""
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr   # Pydantic validates this is a real email format
    password: str = Field(min_length=8, max_length=100)


class UserResponse(BaseModel):
    """What we send back — notice password is NOT here."""
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


# --- Task Schemas (unchanged) ---

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
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