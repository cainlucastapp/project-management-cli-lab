# lib/models/Project.py

# One-to-many: Project -> Tasks

class Project:
    pass


    # Constructor: self, project_id, project_name, project_description, project_due_date, project_status(default: "Active")


    # Property: project_id
        # Must be unique


    # Property: project_name


    # Property: project_description


    # Property: project_due_date
        # Must be a valid date in the format "MM-DD-YYYY"
        # Cannot be a past date


    # Property: project_status
        # Default value is "Active"
        # Can only be "Active" or "Completed"


    # Implement __str__() or __repr__() for clean CLI output.