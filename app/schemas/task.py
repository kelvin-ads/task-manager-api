from pydantic import BaseModel
from typing import Optional


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None


class TaskCreate(TaskBase):
    pass


class TaskResponse(TaskBase):
    id: int
    completed: bool

    class Config:
        from_attributes = True  # Pydantic v2