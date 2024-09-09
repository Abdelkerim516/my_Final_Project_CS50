import pytest
from project import add_task, display_tasks, delete_task, update_task

def test_add_task():
    tasks = []
    add_task(tasks, "Test Task")
    assert tasks == ["Test Task"]

def test_display_tasks(capsys):
    tasks = ["Task 1", "Task 2"]
    display_tasks(tasks)
    captured = capsys.readouterr()
    assert "1. Task 1" in captured.out
    assert "2. Task 2" in captured.out

def test_delete_task():
    tasks = ["Task 1", "Task 2"]
    delete_task(tasks, 1)
    assert tasks == ["Task 2"]

def test_update_task():
    tasks = ["Task 1", "Task 2"]
    update_task(tasks, 1, "Updated Task 1")
    assert tasks == ["Updated Task 1", "Task 2"]


