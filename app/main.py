from fastapi import FastAPI
from routers import tasks

app = FastAPI(title="Task Management API")

# "Include" the tasks router — plugs all its routes into the app
app.include_router(tasks.router)


@app.get("/", tags=["health"])
def root():
    return {"message": "Task API is running 🚀"}