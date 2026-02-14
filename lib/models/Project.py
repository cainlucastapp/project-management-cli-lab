# lib/models/Project.py

# One-to-many: Project -> Tasks

# -------------------------
# Requirements
# -------------------------
import re
from datetime import datetime

# -------------------------
# Project Model
# -------------------------
class Project:

    def __init__(self, id, user_id, title, description, due_date, status):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status


    # -------------------------
    # ID property
    # -------------------------

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        # Must be an integer
        if not isinstance(value, int):
            raise TypeError("ID must be an integer.")
        # Must be greater than 0
        if value <= 0:
            raise ValueError("ID must be greater than 0.")
        self._id = value


    # -------------------------
    # User ID property
    # -------------------------

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        # Must be an integer
        if not isinstance(value, int):
            raise TypeError("User ID must be an integer.")
        # Must be greater than 0
        if value <= 0:
            raise ValueError("User ID must be greater than 0.")
        self._user_id = value


    # -------------------------
    # Title property
    # -------------------------

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # Must be a string
        if not isinstance(value, str):
            raise TypeError("Title must be a string.")
        # Cannot be empty
        if not value.strip():
            raise ValueError("Title cannot be empty.")
        self._title = value


    # -------------------------
    # Description property
    # -------------------------

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        # Must be a string
        if not isinstance(value, str):
            raise TypeError("Description must be a string.")
        # Cannot be empty
        if not value.strip():
            raise ValueError("Description cannot be empty.")
        self._description = value


    # -------------------------
    # Due date property
    # -------------------------

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        # Must be a string
        if not isinstance(value, str):
            raise TypeError("Due date must be a string.")
        # Cannot be empty
        if not value.strip():
            raise ValueError("Due date cannot be empty.")
        # Must be in MM-DD-YYYY format
        if not self._is_valid_date(value):
            raise ValueError("Due date must be in MM-DD-YYYY format.")
        self._due_date = value

    # Validates date format: MM-DD-YYYY
    def _is_valid_date(self, value):
        try:
            datetime.strptime(value, "%m-%d-%Y")
            return True
        except ValueError:
            return False


    # -------------------------
    # Status property
    # -------------------------

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        # Must be a string
        if not isinstance(value, str):
            raise TypeError("Status must be a string.")
        # Must be active or completed
        if value.lower() not in ["active", "completed"]:
            raise ValueError("Status must be 'active' or 'completed'.")
        self._status = value.lower()


    # -------------------------
    # String representation
    # -------------------------

    def __str__(self):
        return f"Project(id={self.id}, user_id={self.user_id}, title='{self.title}', status='{self.status}', due_date='{self.due_date}')"