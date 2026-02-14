# tests/Test_Task.py

# -------------------------
# Requirements
# -------------------------
import pytest
from lib.models.Task import Task


# -------------------------
# Test Task Model: Pass
# -------------------------

def test_task_str():
    task = Task(id=1, project_id=1, title="Implement feature #1", assigned_to="George Heeres", status="active")
    assert str(task) == "Task(id=1, project_id=1, title='Implement feature #1', assigned_to='George Heeres', status='active')"


# -------------------------
# ID errors
# -------------------------

def test_id_not_integer():
    with pytest.raises(TypeError):
        Task(id="one", project_id=1, title="Implement feature #1", assigned_to="George Heeres", status="active")

def test_id_negative():
    with pytest.raises(ValueError):
        Task(id=-1, project_id=1, title="Implement feature #1", assigned_to="George Heeres", status="active")


# -------------------------
# Project ID errors
# -------------------------

def test_project_id_not_integer():
    with pytest.raises(TypeError):
        Task(id=1, project_id="one", title="Implement feature #1", assigned_to="George Heeres", status="active")

def test_project_id_negative():
    with pytest.raises(ValueError):
        Task(id=1, project_id=-1, title="Implement feature #1", assigned_to="George Heeres", status="active")


# -------------------------
# Title errors
# -------------------------

def test_title_not_string():
    with pytest.raises(TypeError):
        Task(id=1, project_id=1, title=123, assigned_to="George Heeres", status="active")

def test_title_empty():
    with pytest.raises(ValueError):
        Task(id=1, project_id=1, title="", assigned_to="George Heeres", status="active")


# -------------------------
# Assigned to errors
# -------------------------

def test_assigned_to_not_string():
    with pytest.raises(TypeError):
        Task(id=1, project_id=1, title="Implement feature #1", assigned_to=123, status="active")

def test_assigned_to_empty():
    with pytest.raises(ValueError):
        Task(id=1, project_id=1, title="Implement feature #1", assigned_to="", status="active")

def test_assigned_to_invalid_characters():
    with pytest.raises(ValueError):
        Task(id=1, project_id=1, title="Implement feature #1", assigned_to="George123", status="active")


# -------------------------
# Status errors
# -------------------------

def test_status_not_string():
    with pytest.raises(TypeError):
        Task(id=1, project_id=1, title="Implement feature #1", assigned_to="George Heeres", status=123)

def test_status_invalid():
    with pytest.raises(ValueError):
        Task(id=1, project_id=1, title="Implement feature #1", assigned_to="George Heeres", status="pending")