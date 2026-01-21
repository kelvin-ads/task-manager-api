from fastapi import APIRouter

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

tasks = []


@router.get("/")
def get_tasks():
    return tasks


@router.post("/")
def create_task(task: dict):
    tasks.append(task)
    return task