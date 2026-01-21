from fastapi import FastAPI
from app.routes import tasks

app = FastAPI(
    title="Task Manager API",
    description="RESTful API for task management",
    version="1.0.0"
)

app.include_router(tasks.router)