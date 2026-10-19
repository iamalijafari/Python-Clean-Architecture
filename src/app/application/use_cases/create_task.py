from app.application.dto.task_dto import TaskDTO
from app.domain.repositories.task_repository import TaskRepository
from app.domain.task import Task


class CreateTask:
    def __init__(self, repository: TaskRepository) -> None:
        self._repository = repository

    def execute(self, title: str) -> TaskDTO:
        task = Task(title)
        created = self._repository.add(task)
        return TaskDTO.model_validate(created)
