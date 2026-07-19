import argparse

from rich import print

from models.project import Project
from models.task import Task
from models.user import User
from utils.storage import load_data, save_data


users = load_data()

parser = argparse.ArgumentParser()

sub = parser.add_subparsers(dest="command")


add_user = sub.add_parser("add-user")
add_user.add_argument("--name", required=True)
add_user.add_argument("--email", required=True)


list_users = sub.add_parser("list-users")


add_project = sub.add_parser("add-project")
add_project.add_argument("--user", required=True)
add_project.add_argument("--title", required=True)
add_project.add_argument("--description", default="")
add_project.add_argument("--due_date", default="")


list_projects = sub.add_parser("list-projects")
list_projects.add_argument("--user", required=True)


add_task = sub.add_parser("add-task")
add_task.add_argument("--project", required=True)
add_task.add_argument("--title", required=True)


complete = sub.add_parser("complete-task")
complete.add_argument("--project", required=True)
complete.add_argument("--title", required=True)


args = parser.parse_args()


if args.command == "add-user":

    users.append(User(args.name, args.email))
    save_data(users)
    print("[green]User added[/green]")


elif args.command == "list-users":

    for user in users:
        print(user)


elif args.command == "add-project":

    for user in users:

        if user.name == args.user:
            user.add_project(
                Project(
                    args.title,
                    args.description,
                    args.due_date
                )
            )

            save_data(users)
            print("[green]Project added[/green]")
            break


elif args.command == "list-projects":

    for user in users:

        if user.name == args.user:

            for project in user.projects:
                print(project)


elif args.command == "add-task":

    for user in users:

        for project in user.projects:

            if project.title == args.project:

                project.add_task(Task(args.title))
                save_data(users)
                print("[green]Task added[/green]")


elif args.command == "complete-task":

    for user in users:

        for project in user.projects:

            if project.title == args.project:

                for task in project.tasks:

                    if task.title == args.title:
                        task.complete()
                        save_data(users)
                        print("[green]Task completed[/green]")