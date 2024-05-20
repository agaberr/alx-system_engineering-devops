#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    request_user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    )
    request_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1])
    )
    user_name = request_user.json()['name']
    todos = request_todos.json()

    total_tasks = len(todos)
    no_tasks_done = 0

    for task in todos:
        if task['completed'] is True:
            no_tasks_done += 1

    print(
            "Employee {} is done with tasks({}/{}):".
            format(user_name, no_tasks_done, total_tasks)
            )

    for task in todos:
        if task['completed'] is True:
            print("\t {}".format(task['title']))
