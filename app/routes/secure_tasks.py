from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.task import Task
from app.schemas.task import TaskResponse
from app.core.deps import get_logged_user

router = APIRouter(
    prefix="/secure-tasks",
    tags=["Secure Tasks"]
)

@router.get("/", response_model=list[TaskResponse])
def list_secure_tasks(
    status: str | None = None,
    priority: str | None = None,
    db: Session = Depends(get_db),
    user=Depends(get_logged_user)
):
    query = db.query(Task).filter(Task.user_id == user.id)

    if status:
        query = query.filter(Task.status == status)

    if priority:
        query = query.filter(Task.priority == priority)

    return query.all()