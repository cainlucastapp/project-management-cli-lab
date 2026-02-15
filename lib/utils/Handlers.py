# lib/utils/Handlers.py

# -------------------------
# Requirements
# -------------------------
from lib.models.User import User
from lib.models.Project import Project
from lib.models.Task import Task
from lib.utils.Helpers import (
    generate_id,
    check_unique_email,
    check_user_exists,
    check_project_exists,
    check_future_date,
    display_success,
    display_error,
    display_view_user
)
from lib.utils.Data_Manager import users, projects, tasks, save_data


# -------------------------
# User handlers
# -------------------------

def handle_add_user(args):
    try:
        # Sanitize input
        name = " ".join(args.name.strip().split())
        email = args.email.strip().lower()

        # Validate business rules
        check_unique_email(users, email)

        # Generate ID and create user
        user = User(
            id=generate_id(users),
            name=name,
            email=email
        )

        # Add to collection and save
        users.append(user)
        save_data()
        display_success(f"User created successfully: {user}")

    except (ValueError, TypeError) as error:
        display_error(str(error))


# -------------------------
# Project handlers
# -------------------------

def handle_add_project(args):
    try:
        # Validate business rules
        check_user_exists(users, args.user_id)
        check_future_date(args.due_date)

        # Generate ID and create project
        project = Project(
            id=generate_id(projects),
            user_id=args.user_id,
            title=args.title.strip(),
            description=args.description.strip(),
            due_date=args.due_date.strip(),
            status="active"
        )

        # Add to collection and save
        projects.append(project)
        save_data()
        display_success(f"Project created successfully: {project}")

    except (ValueError, TypeError) as error:
        display_error(str(error))


# -------------------------
# Task handlers
# -------------------------

def handle_add_task(args):
    try:
        # Validate business rules
        check_project_exists(projects, args.project_id)

        # Sanitize input
        assigned_to = " ".join(args.assigned_to.strip().split())

        # Generate ID and create task
        task = Task(
            id=generate_id(tasks),
            project_id=args.project_id,
            title=args.title.strip(),
            assigned_to=assigned_to,
            status="active"
        )

        # Add to collection and save
        tasks.append(task)
        save_data()
        display_success(f"Task created successfully: {task}")

    except (ValueError, TypeError) as error:
        display_error(str(error))


# -------------------------
# View handlers
# -------------------------

def handle_view_user(args):
    try:
        # Find user by ID
        user = next((u for u in users if u.id == args.id), None)
        if not user:
            raise ValueError(f"No user found with ID {args.id}.")

        # Find projects belonging to this user
        user_projects = [p for p in projects if p.user_id == user.id]

        # Find tasks for each project
        project_tasks = {p.id: [t for t in tasks if t.project_id == p.id] for p in user_projects}

        # Pass to display
        display_view_user(user, user_projects, project_tasks)

    except ValueError as error:
        display_error(str(error))