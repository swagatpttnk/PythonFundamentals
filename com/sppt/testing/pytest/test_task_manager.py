import pytest
from task_manager import TaskManager

# --- Basic Test Functions ---

def test_add_single_task():
    manager = TaskManager()
    manager.add_task("Buy groceries")
    assert manager.get_task_count() == 1
    assert manager.list_tasks() == ["Buy groceries"]

def test_remove_existing_task():
    manager = TaskManager()
    manager.add_task("Walk the dog")
    manager.remove_task("Walk the dog")
    assert manager.get_task_count() == 0
    assert manager.list_tasks() == []

def test_list_empty_tasks():
    manager = TaskManager()
    assert manager.list_tasks() == []

# --- Testing for Expected Exceptions ---

def test_add_duplicate_task_raises_error():
    manager = TaskManager()
    manager.add_task("Read a book")
    with pytest.raises(ValueError) as excinfo:
        manager.add_task("Read a book")
    assert "already exists" in str(excinfo.value) # Check error message

def test_remove_non_existent_task_raises_error():
    manager = TaskManager()
    with pytest.raises(ValueError, match="Task 'NonExistent' not found."): # Match specific message
        manager.remove_task("NonExistent")

def test_add_empty_task_raises_error():
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.add_task("")
    with pytest.raises(ValueError):
        manager.add_task("   ")

