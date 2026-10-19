from uuid import UUID

from pydantic import BaseModel, ConfigDict


class TaskDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    title: str
    is_completed: bool
