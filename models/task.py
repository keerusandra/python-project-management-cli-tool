class Task:

    id_counter = 1

    def __init__(self, title, assigned_to="", status="Pending"):
        self.id = Task.id_counter
        Task.id_counter += 1

        self.title = title
        self.status = status
        self.assigned_to = assigned_to

    def complete(self):
        self.status = "Completed"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(
            data["title"],
            data.get("assigned_to", ""),
            data.get("status", "Pending")
        )
        task.id = data["id"]
        return task

    def __str__(self):
        return f"{self.title} ({self.status})"