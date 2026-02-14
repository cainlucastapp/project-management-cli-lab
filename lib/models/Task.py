# lib/models/Task.py

# One-to-many: Project -> Tasks

# -------------------------
# Requirements
# -------------------------
import re


# -------------------------
# Task Model
# -------------------------
class Task:

    def __init__(self, id, project_id, title, assigned_to, status):
        self.id = id
        self.project_id = project_id
        self.title = title
        self.assigned_to = assigned_to
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
    # Project ID property
    # -------------------------

    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        # Must be an integer
        if not isinstance(value, int):
            raise TypeError("Project ID must be an integer.")
        # Must be greater than 0
        if value <= 0:
            raise ValueError("Project ID must be greater than 0.")
        self._project_id = value


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
    # Assigned to property
    # -------------------------

    @property
    def assigned_to(self):
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, value):
        # Must be a string
        if not isinstance(value, str):
            raise TypeError("Assigned to must be a string.")
        # Cannot be empty
        if not value.strip():
            raise ValueError("Assigned to cannot be empty.")
        # Only letters, spaces, apostrophes, hyphens, and periods
        if not re.fullmatch(r"[A-Za-z][A-Za-z\s'\.\-]*", value):
            raise ValueError("Assigned to may contain letters, spaces, apostrophes, hyphens, and periods only.")
        self._assigned_to = value


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
        return f"Task(id={self.id}, project_id={self.project_id}, title='{self.title}', assigned_to='{self.assigned_to}', status='{self.status}')"