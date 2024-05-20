#!/usr/bin/python3
"""
script that, using this REST API, for all employees,
returns information about his/her TODO list progress,
and export data in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    
    request_user = requests.get('https://jsonplaceholder.typicode.com/users')
    request_todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    todos = request_todos.json()

    user = request_user.json()

    user_name = {user['id']: user['username'] for user in user}


    data = {}

    # { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ...}

    for task in todos:
        user_id = task['userId']
        if user_id not in data:
            data[user_id] = []
        data[user_id].append({
            "task": task['title'],
            "completed": task['completed'],
            "username": user_name[user_id]
        })

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(data, jsonfile)
