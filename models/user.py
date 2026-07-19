from models.person import Person
from models.project import Project


class User(Person):

    id_counter = 1

    def __init__(self, name, email):
        super().__init__(name)

        self.id = User.id_counter
        User.id_counter += 1

        self.email = email
        self.projects = []

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email")
        self._email = value

    def add_project(self, project):
        self.projects.append(project)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "projects": [p.to_dict() for p in self.projects]
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(data["name"], data["email"])
        user.id = data["id"]
        user.projects = [Project.from_dict(p) for p in data["projects"]]
        return user

    def __str__(self):
        return f"{self.name} ({self.email})"