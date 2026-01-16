from fastapi import FastAPI

app = FastAPI(
    title="Task Manager API",
    description="RESTful API for task management",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Task Manager API is running"}