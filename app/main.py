from fastapi import FastAPI
from app.database import engine, Base
from app.routers import tasks

# Creates all tables that don't exist yet — safe to run every time
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management API")
app.include_router(tasks.router)

@app.get("/", tags=["health"])
def root():
    return {"message": "Task API is running 🚀"}