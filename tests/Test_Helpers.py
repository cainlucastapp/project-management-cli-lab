# tests/Test_Helpers.py

# -------------------------
# Requirements
# -------------------------
import pytest
from datetime import datetime, timedelta
from lib.models.User import User
from lib.models.Project import Project
from lib.utils.Helpers import (
    generate_id,
    check_unique_email,
    check_user_exists,
    check_project_exists,
    check_future_date
)


# -------------------------
# Fixtures
# -------------------------

@pytest.fixture
def sample_user():
    return User(id=1, name="George Heeres", email="george.heeres@example.com")

@pytest.fixture
def sample_project():
    return Project(id=1, user_id=1, title="Project #1", description="My first project", due_date="12-31-2026", status="active")

def future_date():
    return (datetime.today() + timedelta(days=30)).strftime("%m-%d-%Y")


# -------------------------
# generate_id tests
# -------------------------

def test_generate_id_empty_collection():
    # Should return 1 for an empty collection
    assert generate_id([]) == 1

def test_generate_id_existing_collection(sample_user):
    # Should return next available ID
    assert generate_id([sample_user]) == 2


# -------------------------
# check_unique_email tests
# -------------------------

def test_check_unique_email_pass(sample_user):
    # Should not raise if email is unique
    check_unique_email([sample_user], "new@example.com")

def test_check_unique_email_fail(sample_user):
    # Should raise if email already exists
    with pytest.raises(ValueError):
        check_unique_email([sample_user], "george.heeres@example.com")


# -------------------------
# check_user_exists tests
# -------------------------

def test_check_user_exists_pass(sample_user):
    # Should not raise if user exists
    check_user_exists([sample_user], 1)

def test_check_user_exists_fail():
    # Should raise if user does not exist
    with pytest.raises(ValueError):
        check_user_exists([], 999)


# -------------------------
# check_project_exists tests
# -------------------------

def test_check_project_exists_pass(sample_project):
    # Should not raise if project exists
    check_project_exists([sample_project], 1)

def test_check_project_exists_fail():
    # Should raise if project does not exist
    with pytest.raises(ValueError):
        check_project_exists([], 999)


# -------------------------
# check_future_date tests
# -------------------------

def test_check_future_date_pass():
    # Should not raise for a future date
    check_future_date(future_date())

def test_check_future_date_fail():
    # Should raise for a past date
    with pytest.raises(ValueError):
        check_future_date("01-01-2000")