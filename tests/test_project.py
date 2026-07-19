import unittest
from models.project import Project
from models.task import Task


class TestProject(unittest.TestCase):

    def test_add_project_task(self):
        project = Project("CLI Tool")
        task = Task("Write README")

        project.add_task(task)

        self.assertEqual(len(project.tasks), 1)
        self.assertEqual(project.tasks[0].title, "Write README")


if __name__ == "__main__":
    unittest.main()