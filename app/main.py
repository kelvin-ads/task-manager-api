from fastapi import FastAPI
from app.database.db import Base, engine

from app.models import task, user  
from app.routes import tasks, users, auth
from app.routes import secure_tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="API segura de gerenciamento de tarefas com autenticação JWT",
    version="1.0.0"
)

app.include_router(tasks.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(secure_tasks.router)
@app.get("/")
def root():
    return {
        "message": "Task Manager API está online 🚀",
        "docs": "/docs"
    }