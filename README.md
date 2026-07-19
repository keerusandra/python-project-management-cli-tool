# python-project-management-cli-tool

A Python command-line application for managing users, projects, and tasks. The application allows administrators to create users, assign projects, add tasks, mark tasks as complete, and save data locally using JSON.

---

## Features

- Create users
- List users
- Add projects to users
- View projects for a specific user
- Add tasks to projects
- Mark tasks as completed
- Store data persistently using JSON
- Command-line interface using `argparse`
- Rich terminal output using the `rich` library

---

## Technologies Used

- Python 3.8.2
- argparse
- JSON
- rich

---

## Project Structure

```text
python-project-management-cli-tool/
│
├── main.py                  # CLI entry point
├── requirements.txt         # Project dependencies
├── README.md                # Project documentation
│
├── models/
│   ├── __init__.py
│   ├── person.py            # Base Person class
│   ├── user.py              # User model
│   ├── project.py           # Project model
│   └── task.py              # Task model
│
├── utils/
│   ├── __init__.py
│   ├── storage.py           # JSON file handling
│   └── helpers.py           # Utility functions
│
├── data/
│   └── database.json        # Persistent application data
│
└── tests/
    ├── __init__.py
    ├── test_user.py
    ├── test_project.py
    └── test_task.py
```

---

## Installation

1. Clone the repository.

```bash
git clone https://github.com/keerusandra/python-project-management-cli-tool.git
```

2. Navigate into the project.

```bash
cd python-project-management-cli-tool
```

3. Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Running the Application

### Add a user

```bash
python main.py add-user --name "Alex" --email "alex@example.com"
```

### List users

```bash
python main.py list-users
```

### Add a project

```bash
python main.py add-project --user "Alex" --title "CLI Tool" --description "Python project" --due_date "2026-08-01"
```

### List projects

```bash
python main.py list-projects --user "Alex"
```

### Add a task

```bash
python main.py add-task --project "CLI Tool" --title "Implement add-task"
```

### Complete a task

```bash
python main.py complete-task --project "CLI Tool" --title "Implement add-task"
```

---

## Object-Oriented Programming Concepts

This project demonstrates:

- Classes and objects
- Inheritance (`Person → User`)
- One-to-many relationships
- Properties and setters
- Class attributes
- Instance methods
- JSON serialization
- File I/O
- Exception handling

---

## Data Storage

All application data is stored in:

```
data/database.json
```

The file is automatically updated whenever users, projects, or tasks are modified.

---

## Future Improvements

- Delete users, projects, and tasks
- Edit project details
- Search functionality
- Due-date reminders
- User authentication
- Unit testing with pytest

---

## Author

SK
