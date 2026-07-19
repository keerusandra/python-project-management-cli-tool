# utils/helpers.py

def find_user(users, name):
    """Find a user by name."""
    return next((user for user in users if user.name.lower() == name.lower()), None)


def find_project(user, title):
    """Find a project belonging to a user."""
    return next((project for project in user.projects if project.title.lower() == title.lower()), None)


def find_task(project, title):
    """Find a task in a project."""
    return next((task for task in project.tasks if task.title.lower() == title.lower()), None)