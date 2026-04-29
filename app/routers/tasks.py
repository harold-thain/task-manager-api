from fastapi import APIRouter, HTTPException
from models import TaskCreate, TaskResponse

router = APIRouter(
    prefix="/tasks",   # every route in here starts with /tasks
    tags=["tasks"],    # groups them nicely in /docs
)

# --- In-memory "database" ---
# A simple list acting as our data store for now.
# Each item will be a dict. We track IDs with a counter.
tasks_db: list[dict] = []
next_id: int = 1


@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate):
    """
    Create a new task.
    Status 201 = "Created" (more specific than 200 for creation).
    """
    global next_id
    new_task = {
        "id": next_id,
        **task.model_dump()   # unpacks all fields from the Pydantic model into the dict
    }
    tasks_db.append(new_task)
    next_id += 1
    return new_task


@router.get("/", response_model=list[TaskResponse])
def get_all_tasks():
    """Return every task. Later, this will be filtered by logged-in user."""
    return tasks_db


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    """Get a single task by ID. 404 if it doesn't exist."""
    for task in tasks_db:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, updated: TaskCreate):
    """
    Replace a task's data entirely.
    We find it, overwrite its fields, keep the same ID.
    """
    for index, task in enumerate(tasks_db):
        if task["id"] == task_id:
            tasks_db[index] = {"id": task_id, **updated.model_dump()}
            return tasks_db[index]
    raise HTTPException(status_code=404, detail="Task not found")


@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int):
    """
    Delete a task. Status 204 = "No Content" — success, but nothing to return.
    """
    for index, task in enumerate(tasks_db):
        if task["id"] == task_id:
            tasks_db.pop(index)
            return
    raise HTTPException(status_code=404, detail="Task not found")