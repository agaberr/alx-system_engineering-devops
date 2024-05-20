#!/usr/bin/python3
"""
A sript that, uses a REST API, for a given employee ID, returns
information about his/her TODO list progress
and exports data in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    request_user = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'
            .format(argv[1])
            )
    request_todos = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(argv[1])
            )

    user_name = request_user.json()['name']
    todos = request_todos.json()


# { "USER_ID": [{"task": "TASK_TITLE",
# "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
# {"task": "TASK_TITLE",
# "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}

file_name = "{}.json".format(argv[1])
data = []

for task in todos:
    data.append({
        "task": task['title'],
        "completed": task['completed'],
        "username": user_name
        })

data_id = {argv[1]: data}

with open(file_name, 'w') as jsonfile:
    json.dump(data_id, jsonfile)
