# lib/utilities/data_manager.py

# -------------------------
# Requirements
# -------------------------
import json
import os
from lib.models.User import User
from lib.models.Project import Project
from lib.models.Task import Task

# -------------------------
# Data file path
# -------------------------
DATA_FILE = "data/data.json"

# -------------------------
# In-memory collections
# -------------------------
users = []
projects = []
tasks = []


# -------------------------
# Convert objects to dictionaries for JSON storage
# -------------------------

def user_to_dict(user):
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }

def project_to_dict(project):
    return {
        "id": project.id,
        "user_id": project.user_id,
        "title": project.title,
        "description": project.description,
        "due_date": project.due_date,
        "status": project.status
    }

def task_to_dict(task):
    return {
        "id": task.id,
        "project_id": task.project_id,
        "title": task.title,
        "assigned_to": task.assigned_to,
        "status": task.status
    }


# -------------------------
# Rebuild objects from dictionaries loaded from JSON
# -------------------------

def dict_to_user(data):
    return User(
        id=data["id"],
        name=data["name"],
        email=data["email"]
    )

def dict_to_project(data):
    return Project(
        id=data["id"],
        user_id=data["user_id"],
        title=data["title"],
        description=data["description"],
        due_date=data["due_date"],
        status=data["status"]
    )

def dict_to_task(data):
    return Task(
        id=data["id"],
        project_id=data["project_id"],
        title=data["title"],
        assigned_to=data["assigned_to"],
        status=data["status"]
    )


# -------------------------
# Load data from JSON file
# -------------------------

def load_data():
    # If file does not exist, start with empty collections
    if not os.path.exists(DATA_FILE):
        return

    # If file is empty, start with empty collections
    if os.path.getsize(DATA_FILE) == 0:
        return

    # If file is malformed, start with empty collections
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("Warning: data file is malformed, starting with empty collections.")
        return

    # Rebuild collections from dictionaries
    users.clear()
    projects.clear()
    tasks.clear()

    users.extend([dict_to_user(u) for u in data.get("users", [])])
    projects.extend([dict_to_project(p) for p in data.get("projects", [])])
    tasks.extend([dict_to_task(t) for t in data.get("tasks", [])])


# -------------------------
# Save data to JSON file
# -------------------------

def save_data():
    # Create the data directory if it does not exist
    os.makedirs("data", exist_ok=True)

    data = {
        "users": [user_to_dict(u) for u in users],
        "projects": [project_to_dict(p) for p in projects],
        "tasks": [task_to_dict(t) for t in tasks]
    }

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)