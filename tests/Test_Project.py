# tests/Test_Project.py


# -------------------------
# Requirements
# -------------------------
import pytest
from lib.models.Project import Project


# -------------------------
# Test Project Model: Pass
# -------------------------

def test_project_str():
    project = Project(id=1, user_id=1, title="Project #1", description="My first project", due_date="12-31-2026", status="active")
    assert str(project) == "Project(id=1, user_id=1, title='Project #1', status='active', due_date='12-31-2026')"


# -------------------------
# ID errors
# -------------------------

def test_id_not_integer():
    with pytest.raises(TypeError):
        Project(id="one", user_id=1, title="Project #1", description="My first project", due_date="12-31-2026", status="active")

def test_id_negative():
    with pytest.raises(ValueError):
        Project(id=-1, user_id=1, title="Project #1", description="My first project", due_date="12-31-2026", status="active")


# -------------------------
# User ID errors
# -------------------------

def test_user_id_not_integer():
    with pytest.raises(TypeError):
        Project(id=1, user_id="one", title="Project #1", description="My first project", due_date="12-31-2026", status="active")

def test_user_id_negative():
    with pytest.raises(ValueError):
        Project(id=1, user_id=-1, title="Project #1", description="My first project", due_date="12-31-2026", status="active")


# -------------------------
# Title errors
# -------------------------

def test_title_not_string():
    with pytest.raises(TypeError):
        Project(id=1, user_id=1, title=123, description="My first project", due_date="12-31-2026", status="active")

def test_title_empty():
    with pytest.raises(ValueError):
        Project(id=1, user_id=1, title="", description="My first project", due_date="12-31-2026", status="active")


# -------------------------
# Description errors
# -------------------------

def test_description_not_string():
    with pytest.raises(TypeError):
        Project(id=1, user_id=1, title="Project #1", description=123, due_date="12-31-2026", status="active")

def test_description_empty():
    with pytest.raises(ValueError):
        Project(id=1, user_id=1, title="Project #1", description="", due_date="12-31-2026", status="active")


# -------------------------
# Due date errors
# -------------------------

def test_due_date_not_string():
    with pytest.raises(TypeError):
        Project(id=1, user_id=1, title="Project #1", description="My first project", due_date=12312026, status="active")

def test_due_date_empty():
    with pytest.raises(ValueError):
        Project(id=1, user_id=1, title="Project #1", description="My first project", due_date="", status="active")

def test_due_date_invalid_format():
    with pytest.raises(ValueError):
        Project(id=1, user_id=1, title="Project #1", description="My first project", due_date="2026-12-31", status="active")


# -------------------------
# Status errors
# -------------------------

def test_status_not_string():
    with pytest.raises(TypeError):
        Project(id=1, user_id=1, title="Project #1", description="My first project", due_date="12-31-2026", status=123)

def test_status_invalid():
    with pytest.raises(ValueError):
        Project(id=1, user_id=1, title="Project #1", description="My first project", due_date="12-31-2026", status="pending")