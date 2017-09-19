#!/usr/bin/python3
"""
using https://jsonplaceholder.typicode.com/ REST API, for a given
employee ID, returns information about his/her TODO list progress
"""
import requests
import sys


def make_request(data, num):
    """
    makes employee request and returns json dict response
    """
    root = 'https://jsonplaceholder.typicode.com'
    url = '{}{}{}'.format(root, data, num)
    return requests.get(url).json()


def app(num):
    """
    makes request for info about employee todo list, then prints
    """
    employee = make_request('/users/', num)
    todos = make_request('/todos/?userId=', num)
    completed = [t.get('title') for t in todos if t.get('completed')]
    total = len(todos)
    print('Employee {} is done with tasks({}/{}):'.format(
        employee.get('name'), len(completed), total))
    for t in completed:
        print('\t {}'.format(t))


if __name__ == '__main__':
    """
    MAIN App
    """
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        app(sys.argv[1])
