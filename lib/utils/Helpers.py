# lib/utils/Helpers.py

# -------------------------
# Requirements
# -------------------------
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich import box

# -------------------------
# Rich console instance
# -------------------------
console = Console()


# -------------------------
# ID generation
# -------------------------

def generate_id(collection):
    # Generate the next available ID based on the current collection
    if not collection:
        return 1
    return max(obj.id for obj in collection) + 1


# -------------------------
# Validations
# -------------------------

def check_unique_email(users, email):
    # Email must be unique across all users
    if any(u.email == email for u in users):
        raise ValueError(f"Email '{email}' is already in use.")

def check_user_exists(users, user_id):
    # User must exist before adding a project
    if not any(u.id == user_id for u in users):
        raise ValueError(f"No user found with ID {user_id}.")

def check_project_exists(projects, project_id):
    # Project must exist before adding a task
    if not any(p.id == project_id for p in projects):
        raise ValueError(f"No project found with ID {project_id}.")

def check_future_date(due_date):
    # Due date cannot be in the past
    parsed_date = datetime.strptime(due_date, "%m-%d-%Y")
    if parsed_date.date() < datetime.today().date():
        raise ValueError("Due date cannot be in the past.")


# -------------------------
# Display
# -------------------------

def display_success(message):
    # Display a success message in green
    console.print(f"[green]{message}[/green]")

def display_error(message):
    # Display an error message in red
    console.print(f"[red]Error:[/red] {message}")

def display_view_user(user, user_projects, project_tasks):
    # Print user header
    console.print(f"\n[bold cyan]User ID: {user.id}[/bold cyan] | Name: {user.name} | Email: {user.email}")
    console.rule()

    # No projects found
    if not user_projects:
        console.print("[yellow]No projects found for this user.[/yellow]")
        return

    # Loop through each project
    for project in user_projects:
        # Print project info
        console.print(f"\n[bold green]Project [ID: {project.id}][/bold green] | {project.title} | [yellow]{project.status.upper()}[/yellow] | Due: {project.due_date}")
        console.print(f"[bold]Description:[/bold] [italic]{project.description}[/italic]\n")

        # Get tasks for this project
        tasks = project_tasks.get(project.id, [])

        # No tasks found
        if not tasks:
            console.print("[yellow]  No tasks found for this project.[/yellow]")
        else:
            # Build task table
            task_table = Table(box=box.SIMPLE_HEAVY, show_header=True)
            task_table.add_column("Task ID", style="cyan", justify="center")
            task_table.add_column("Title", style="white")
            task_table.add_column("Status", style="yellow")
            task_table.add_column("Assigned To", style="green")

            # Add a row for each task
            for task in tasks:
                task_table.add_row(
                    str(task.id),
                    task.title,
                    task.status,
                    task.assigned_to
                )

            console.print(task_table)

        console.rule()