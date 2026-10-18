from uuid import UUID

import pytest

from app.domain.task import Task


def test_task_is_created_with_valid_title():
    task = Task("Learn Python")

    assert isinstance(task.id, UUID)
    assert task.title == "Learn Python"
    assert task.is_completed is False


def test_task_strips_whitespace_from_title():
    task = Task("  Learn Python  ")

    assert task.title == "Learn Python"


@pytest.mark.parametrize("title", ["", "   ", "\t\n"])
def test_task_rejects_empty_or_whitespace_title(title: str):
    with pytest.raises(ValueError, match="Task title cannot be empty."):
        Task(title)


def test_task_can_be_created_with_existing_id():
    task_id = UUID("12345678-1234-5678-1234-567812345678")

    task = Task("Learn Python", task_id=task_id)

    assert task.id == task_id
