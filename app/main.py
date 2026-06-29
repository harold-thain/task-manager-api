from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.database import engine, Base
from app.routers import tasks, users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

app.include_router(users.router)
app.include_router(tasks.router)

# Client gets nice response, we still have stacktrace on production side
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "An internal server error occurred"}
    )

@app.get("/", tags=["health"])
def root():
    return {"message": "Task API is running 🚀"}