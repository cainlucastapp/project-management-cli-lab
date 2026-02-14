# lib/models/User.py

# One-to-many: User -> Projects

# -------------------------
# Requirements
# -------------------------
import re


# -------------------------
# User Model
# -------------------------
class User:

    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email


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
    # Name property
    # -------------------------

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Must be a string
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        # Cannot be empty
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        # Only letters, spaces, apostrophes, hyphens, and periods
        if not re.fullmatch(r"[A-Za-z][A-Za-z\s'\.\-]*", value):
            raise ValueError("Name may contain letters, spaces, apostrophes, hyphens, and periods only.")
        self._name = value


    # -------------------------
    # Email property
    # -------------------------

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        # Must be a string
        if not isinstance(value, str):
            raise TypeError("Email must be a string.")
        # Cannot be empty
        if not value.strip():
            raise ValueError("Email cannot be empty.")
        # Must be a valid email format
        if not self._is_valid_email(value):
            raise ValueError("Email must be a valid email address.")
        self._email = value

    # Validates email format: email@something.com
    def _is_valid_email(self, value):
        return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", value))


    # -------------------------
    # String representation
    # -------------------------

    def __str__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"