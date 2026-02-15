# tests/Test_Handlers.py

# -------------------------
# Requirements
# -------------------------
import pytest
from unittest.mock import patch, MagicMock
from lib.models.User import User
from lib.models.Project import Project
from lib.models.Task import Task


# -------------------------
# Fixtures
# -------------------------

@pytest.fixture
def sample_user():
    return User(id=1, name="George Heeres", email="george.heeres@example.com")

@pytest.fixture
def sample_project():
    return Project(id=1, user_id=1, title="Project #1", description="My first project", due_date="12-31-2026", status="active")

@pytest.fixture
def sample_task():
    return Task(id=1, project_id=1, title="Implement feature #1", assigned_to="George Heeres", status="active")


# -------------------------
# handle_add_user tests
# -------------------------

def test_handle_add_user_success(sample_user):
    # User should be added to the collection successfully
    args = MagicMock()
    args.name = "George Heeres"
    args.email = "george.heeres@example.com"

    with patch("lib.utils.Handlers.users", []) as mock_users, \
         patch("lib.utils.Handlers.save_data"), \
         patch("lib.utils.Handlers.display_success"):
        from lib.utils.Handlers import handle_add_user
        handle_add_user(args)
        assert len(mock_users) == 1

def test_handle_add_user_duplicate_email(sample_user):
    # Duplicate email should display an error
    args = MagicMock()
    args.name = "George Heeres"
    args.email = "george.heeres@example.com"

    with patch("lib.utils.Handlers.users", [sample_user]), \
         patch("lib.utils.Handlers.save_data"), \
         patch("lib.utils.Handlers.display_error") as mock_error:
        from lib.utils.Handlers import handle_add_user
        handle_add_user(args)
        mock_error.assert_called_once()


# -------------------------
# handle_add_project tests
# -------------------------

def test_handle_add_project_success(sample_user):
    # Project should be added to the collection successfully
    args = MagicMock()
    args.user_id = 1
    args.title = "Project #1"
    args.description = "My first project"
    args.due_date = "12-31-2026"

    with patch("lib.utils.Handlers.users", [sample_user]), \
         patch("lib.utils.Handlers.projects", []) as mock_projects, \
         patch("lib.utils.Handlers.save_data"), \
         patch("lib.utils.Handlers.display_success"):
        from lib.utils.Handlers import handle_add_project
        handle_add_project(args)
        assert len(mock_projects) == 1

def test_handle_add_project_user_not_found():
    # Project should not be added if user does not exist
    args = MagicMock()
    args.user_id = 999
    args.title = "Project #1"
    args.description = "My first project"
    args.due_date = "12-31-2026"

    with patch("lib.utils.Handlers.users", []), \
         patch("lib.utils.Handlers.display_error") as mock_error:
        from lib.utils.Handlers import handle_add_project
        handle_add_project(args)
        mock_error.assert_called_once()


# -------------------------
# handle_add_task tests
# -------------------------

def test_handle_add_task_success(sample_project):
    # Task should be added to the collection successfully
    args = MagicMock()
    args.project_id = 1
    args.title = "Implement feature #1"
    args.assigned_to = "George Heeres"

    with patch("lib.utils.Handlers.projects", [sample_project]), \
         patch("lib.utils.Handlers.tasks", []) as mock_tasks, \
         patch("lib.utils.Handlers.save_data"), \
         patch("lib.utils.Handlers.display_success"):
        from lib.utils.Handlers import handle_add_task
        handle_add_task(args)
        assert len(mock_tasks) == 1

def test_handle_add_task_project_not_found():
    # Task should not be added if project does not exist
    args = MagicMock()
    args.project_id = 999
    args.title = "Implement feature #1"
    args.assigned_to = "George Heeres"

    with patch("lib.utils.Handlers.projects", []), \
         patch("lib.utils.Handlers.display_error") as mock_error:
        from lib.utils.Handlers import handle_add_task
        handle_add_task(args)
        mock_error.assert_called_once()


# -------------------------
# handle_view_user tests
# -------------------------

def test_handle_view_user_success(sample_user):
    # View user should call display_view_user with correct data
    args = MagicMock()
    args.id = 1

    with patch("lib.utils.Handlers.users", [sample_user]), \
         patch("lib.utils.Handlers.projects", []), \
         patch("lib.utils.Handlers.tasks", []), \
         patch("lib.utils.Handlers.display_view_user") as mock_display:
        from lib.utils.Handlers import handle_view_user
        handle_view_user(args)
        mock_display.assert_called_once()

def test_handle_view_user_not_found():
    # View user should display error if user not found
    args = MagicMock()
    args.id = 999

    with patch("lib.utils.Handlers.users", []), \
         patch("lib.utils.Handlers.display_error") as mock_error:
        from lib.utils.Handlers import handle_view_user
        handle_view_user(args)
        mock_error.assert_called_once()