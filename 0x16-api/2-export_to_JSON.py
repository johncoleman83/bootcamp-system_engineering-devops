#!/usr/bin/python3
"""
using https://jsonplaceholder.typicode.com/ REST API, for a given
employee ID, returns information about his/her TODO list progress
"""
import sys
import requests
import json


def make_request(data, num):
    """
    makes employee request and returns json dict response
    """
    root = 'https://jsonplaceholder.typicode.com'
    url = root + data + num
    return requests.get(url).json()


def app():
    """
    request for info about employee todo list, writes to .json file
    """
    num = str(sys.argv[1])
    employee = make_request('/users/', num)
    todos = make_request('/todos/?userId=', num)
    all_tasks = [
        {'task': t.get('title'), 'completed': t.get('completed')}
        for t in todos
    ]
    user_data = {num: all_tasks}
    filename = num + '.json'
    with open(filename, 'w') as jsonfile:
        jsonfile.write(json.dumps(user_data))


if __name__ == '__main__':
    """
    MAIN App
    """
    app()
