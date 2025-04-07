import pytest
import json
import os
from task_tracker import Task

@pytest.fixture
def task_manager():
    test_file = 'test_tasks.json'
    initial_data = {"tasks": []}
    with open(test_file, 'w') as f:
        json.dump(initial_data, f)


    with open(test_file, 'r') as f:
        tasks_dict = json.load(f)
    task_manager = Task(tasks_dict)

    yield task_manager


    if os.path.exists(test_file):
        os.remove(test_file)

def test_add_task(task_manager):
    task_manager.add_task("Test Task 1")
    assert len(task_manager.tasks_dict["tasks"]) == 1
    assert task_manager.tasks_dict["tasks"][0]["task"] == "Test Task 1"

def test_view_tasks(task_manager):
    task_manager.add_task("Test Task 1")
    task_manager.add_task("Test Task 2")
    assert len(task_manager.tasks_dict["tasks"]) == 2

def test_delete_task(task_manager):
    task_manager.add_task("Test Task 1")
    task_manager.add_task("Test Task 2")
    task_manager.delete_task(1)
    assert len(task_manager.tasks_dict["tasks"]) == 1
    assert task_manager.tasks_dict["tasks"][0]["task"] == "Test Task 2"

def test_update_task(task_manager):
    task_manager.add_task("Test Task 1")
    task_manager.update_task(1, "Updated Task 1")
    assert task_manager.tasks_dict["tasks"][0]["task"] == "Updated Task 1"

def test_update_status(task_manager):
    task_manager.add_task("Test Task 1")
    task_manager.update_status(1, "done")
    assert task_manager.tasks_dict["tasks"][0]["status"] == "done"