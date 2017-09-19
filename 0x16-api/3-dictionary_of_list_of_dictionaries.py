#!/usr/bin/python3
"""
using https://jsonplaceholder.typicode.com/ REST API, for a given
employee ID, returns information about his/her TODO list progress
"""
import requests
import json


def make_request(data, num):
    """
    makes employee request and returns json dict response
    """
    root = 'https://jsonplaceholder.typicode.com'
    url = '{}{}{}'.format(root, data, num)
    return requests.get(url).json()


def app():
    """
    writes all employee data to .json file
    """
    all_employee_data = {}
    u_url = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(u_url).json()
    for user in users:
        num = str(user.get('id'))
        username = user.get('username')
        todos = make_request('/todos/?userId=', num)
        all_tasks = [
            {'username': username,
             'task': t.get('title'),
             'completed': t.get('completed')}
            for t in todos
        ]
        all_employee_data[num] = all_tasks
    filename = 'todo_all_employees.json'
    with open(filename, 'w') as jsonfile:
        jsonfile.write(json.dumps(all_employee_data, sort_keys=True))


if __name__ == '__main__':
    """
    MAIN App
    """
    app()
