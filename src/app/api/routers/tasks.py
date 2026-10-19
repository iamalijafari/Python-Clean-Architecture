from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import get_task_repository
from app.api.schemas.task import CreateTaskRequest, TaskResponse
from app.application.use_cases.complete_task import CompleteTask
from app.application.use_cases.create_task import CreateTask
from app.application.use_cases.delete_task import DeleteTask
from app.application.use_cases.get_task import GetTask
from app.application.use_cases.list_tasks import ListTasks
from app.infrastructure.repositories.task_repository import SqlAlchemyTaskRepository

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
    request: CreateTaskRequest,
    repository: SqlAlchemyTaskRepository = Depends(get_task_repository),
) -> TaskResponse:
    return CreateTask(repository).execute(request.title)


@router.get("", response_model=list[TaskResponse])
def list_tasks(
    repository: SqlAlchemyTaskRepository = Depends(get_task_repository),
) -> list[TaskResponse]:
    return ListTasks(repository).execute()


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: UUID,
    repository: SqlAlchemyTaskRepository = Depends(get_task_repository),
) -> TaskResponse:
    task = GetTask(repository).execute(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.patch("/{task_id}/complete", response_model=TaskResponse)
def complete_task(
    task_id: UUID,
    repository: SqlAlchemyTaskRepository = Depends(get_task_repository),
) -> TaskResponse:
    task = CompleteTask(repository).execute(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: UUID,
    repository: SqlAlchemyTaskRepository = Depends(get_task_repository),
) -> None:
    deleted = DeleteTask(repository).execute(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
