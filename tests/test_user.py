import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def test_create_user(self):
        user = User("Alex", "alex@example.com")

        self.assertEqual(user.name, "Alex")
        self.assertEqual(user.email, "alex@example.com")
        self.assertEqual(len(user.projects), 0)

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            User("Alex", "invalidemail")


if __name__ == "__main__":
    unittest.main()