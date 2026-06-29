from fastapi import FastAPI
from app.database import engine, Base
from app.routers import tasks, users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management API")

app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/", tags=["health"])
def root():
    return {"message": "Task API is running 🚀"}