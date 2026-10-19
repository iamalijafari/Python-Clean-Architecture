from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class CreateTaskRequest(BaseModel):
    title: str = Field(min_length=1, max_length=200)


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    title: str
    is_completed: bool
