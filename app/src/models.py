from pydantic import BaseModel, Field

class Task(BaseModel):
    id: int | None = None
    title: str = Field(..., min_length=3)
    description: str | None = None
    completed: bool = None