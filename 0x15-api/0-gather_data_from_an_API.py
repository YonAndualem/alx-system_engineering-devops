#!/usr/bin/python3
"""0-gather_data_from_an_API model
"""
import json
import requests
from sys import argv

BASE_URL = "https://jsonplaceholder.typicode.com"


class Todo:
    """Todo Class
    """

    def __init__(self, userId, id, title, completed):
        """initializes a todo class

        Args:
            userId (int): the user id
            id (id): the task id
            title (str): the task title
            completed (boolean): boolean completed flag
        """
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed


class User:
    """user class
    """

    def __init__(self, id, name):
        """initializes a user class

        Args:
            id (int): the user id
            name (str): the user name
        """
        self.id = id
        self.name = name


def get_employee_todos(id):
    """gets employee data

    Args:
        id (int): the employee id

    Returns:
        list | None: list of todos or None
    """
    result = requests.get("{}/todos?userId={}".format(BASE_URL, id))
    if result.status_code == 200:
        todos = json.loads(result.text)
        return [Todo(**todo) for todo in todos]


def get_user_info(id):
    """gets user information

    Args:
        id (int): the user id

    Returns:
        User | None: user or None
    """
    result = requests.get("{}/users/{}".format(BASE_URL, id))
    if result.status_code == 200:
        user_data = json.loads(result.text)
        return User(
            id=user_data["id"],
            name=user_data["name"],
        )


def print_employee_todos(employee, todos):
    """prints employee completed todos

    Args:
        employee (user): user
        todos (list(todo)): list of todos
    """
    done_todos = [todo for todo in todos if todo.completed]
    total_count = len(todos)
    done_count = len(done_todos)
    print("Employee {} is done with tasks({}/{}):".format(
        employee.name,
        done_count,
        total_count,
    ))
    for todo in done_todos:
        print("\t {}".format(todo.title))


if __name__ == "__main__":
    if (len(argv) > 1 and argv[1].isdigit()):
        todos = get_employee_todos(int(argv[1]))
        employee = get_user_info(argv[1])
        print_employee_todos(employee, todos)
