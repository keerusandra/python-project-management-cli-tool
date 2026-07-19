import json
import os

from models.user import User

FILE = "data/database.json"


def load_data():

    if not os.path.exists(FILE):
        return []

    try:
        with open(FILE, "r") as f:
            data = json.load(f)

        return [User.from_dict(user) for user in data["users"]]

    except (json.JSONDecodeError, KeyError):
        return []


def save_data(users):

    with open(FILE, "w") as f:
        json.dump(
            {
                "users": [user.to_dict() for user in users]
            },
            f,
            indent=4
        )