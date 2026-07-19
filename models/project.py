from models.task import Task


class Project:

    id_counter = 1

    def __init__(self, title, description="", due_date=""):
        self.id = Project.id_counter
        Project.id_counter += 1

        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "tasks": [task.to_dict() for task in self.tasks]
        }

    @classmethod
    def from_dict(cls, data):
        project = cls(
            data["title"],
            data.get("description", ""),
            data.get("due_date", "")
        )

        project.id = data["id"]
        project.tasks = [Task.from_dict(t) for t in data["tasks"]]
        return project

    def __str__(self):
        return self.title