import argparse

from rich import print

from models.user import User
from models.project import Project
from models.task import Task
from utils.storage import load_data, save_data
from utils.helpers import find_user, find_project, find_task


def main():
    users = load_data()

    parser = argparse.ArgumentParser(
        description="Project Tracker CLI"
    )

    subparsers = parser.add_subparsers(dest="command")

    add_user = subparsers.add_parser("add-user")
    add_user.add_argument("--name", required=True)
    add_user.add_argument("--email", required=True)

    subparsers.add_parser("list-users")

    add_project = subparsers.add_parser("add-project")
    add_project.add_argument("--user", required=True)
    add_project.add_argument("--title", required=True)
    add_project.add_argument("--description", default="")
    add_project.add_argument("--due_date", default="")

    list_projects = subparsers.add_parser("list-projects")
    list_projects.add_argument("--user", required=True)

    add_task = subparsers.add_parser("add-task")
    add_task.add_argument("--user", required=True)
    add_task.add_argument("--project", required=True)
    add_task.add_argument("--title", required=True)

    complete_task = subparsers.add_parser("complete-task")
    complete_task.add_argument("--user", required=True)
    complete_task.add_argument("--project", required=True)
    complete_task.add_argument("--title", required=True)

    args = parser.parse_args()

    if args.command == "add-user":

        if find_user(users, args.name):
            print("[red]User already exists.[/red]")
            return

        user = User(args.name, args.email)
        users.append(user)
        save_data(users)

        print(f"[green]User '{args.name}' added successfully![/green]")

    elif args.command == "list-users":

        if not users:
            print("[yellow]No users found.[/yellow]")
            return

        for user in users:
            print(user)

    elif args.command == "add-project":

        user = find_user(users, args.user)

        if not user:
            print("[red]User not found.[/red]")
            return

        project = Project(
            args.title,
            args.description,
            args.due_date
        )

        user.add_project(project)

        save_data(users)

        print(f"[green]Project '{args.title}' added to {user.name}.[/green]")

    elif args.command == "list-projects":

        user = find_user(users, args.user)

        if not user:
            print("[red]User not found.[/red]")
            return

        if not user.projects:
            print("[yellow]No projects found.[/yellow]")
            return

        for project in user.projects:
            print(project)

    elif args.command == "add-task":

        user = find_user(users, args.user)

        if not user:
            print("[red]User not found.[/red]")
            return

        project = find_project(user, args.project)

        if not project:
            print("[red]Project not found.[/red]")
            return

        project.add_task(Task(args.title))

        save_data(users)

        print(f"[green]Task '{args.title}' added successfully.[/green]")

    elif args.command == "complete-task":

        user = find_user(users, args.user)

        if not user:
            print("[red]User not found.[/red]")
            return

        project = find_project(user, args.project)

        if not project:
            print("[red]Project not found.[/red]")
            return

        task = find_task(project, args.title)

        if not task:
            print("[red]Task not found.[/red]")
            return

        task.complete()

        save_data(users)

        print(f"[green]Task '{args.title}' marked as completed.[/green]")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()