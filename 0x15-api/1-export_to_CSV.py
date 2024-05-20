#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress,
And then export data in the CSV format.
"""

import csv
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

    user_name = request_user.json()['username']
    todos = request_todos.json()

    # "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    data = []
    for task in todos:
        data.append({
            'USER_ID': argv[1],
            'USERNAME': user_name,
            'TASK_COMPLETED_STATUS': task['completed'],
            'TASK_TITLE': task['title']
        })

    file_name = "{}.csv".format(argv[1])
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)

        for task in data:
            writer.writerow(
                    [task['USER_ID'], task['USERNAME'],
                        task['TASK_COMPLETED_STATUS'], task['TASK_TITLE']]
                    )
