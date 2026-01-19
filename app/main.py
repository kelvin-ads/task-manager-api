from fastapi import FastAPI

app = FastAPI(
    title="Task Manager API",
    description="RESTful API for task management",
    version="1.0.0"
)

tasks = []

@app.get("/")
def read_root():
    return {"message": "Task Manager API is running"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: dict):
    tasks.append(task)
    return task