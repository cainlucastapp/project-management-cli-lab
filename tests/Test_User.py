# tests/Test_User.py


# -------------------------
# Requirements
# -------------------------
import pytest
from lib.models.User import User


# -------------------------
# Test User Model: Pass
# -------------------------

def test_user_str():
    user = User(id=1, name="George Heeres", email="george.heeres@example.com")
    assert str(user) == "User(id=1, name='George Heeres', email='george.heeres@example.com')"


# -------------------------
# ID errors
# -------------------------

def test_id_not_integer():
    with pytest.raises(TypeError):
        User(id="one", name="George Heeres", email="george.heeres@example.com")

def test_id_negative():
    with pytest.raises(ValueError):
        User(id=-1, name="George Heeres", email="george.heeres@example.com")


# -------------------------
# Name errors
# -------------------------

def test_name_not_string():
    with pytest.raises(TypeError):
        User(id=1, name=123, email="george.heeres@example.com")

def test_name_empty():
    with pytest.raises(ValueError):
        User(id=1, name="", email="george.heeres@example.com")

def test_name_invalid_characters():
    with pytest.raises(ValueError):
        User(id=1, name="George123", email="george.heeres@example.com")


# -------------------------
# Email errors
# -------------------------

def test_email_not_string():
    with pytest.raises(TypeError):
        User(id=1, name="George Heeres", email=123)

def test_email_empty():
    with pytest.raises(ValueError):
        User(id=1, name="George Heeres", email="")

def test_email_invalid_format():
    with pytest.raises(ValueError):
        User(id=1, name="George Heeres", email="notanemail")