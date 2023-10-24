#!/usr/bin/python3
"""fetch ifo by employee ID."""

import requests
import sys


def fetch_json(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()


def todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'

    user_data = fetch_json(f'{base_url}/users/{employee_id}')
    if user_data is None:
        print(f"Error: Could not retrieve user data for ID {employee_id}")
        return

    user_name = user_data.get('name')
    if not user_name:
        print(f"Error: User name not found for ID {employee_id}")
        return

    todo_data = fetch_json(f'{base_url}/todos?userId={employee_id}')
    if not todo_data:
        print(f"No TODO list data found for user ID {employee_id}")
        return

    total_tasks = len(todo_data)
    completed_tasks = sum(1 for todo in todo_data if todo.get('completed'))

    print(f"Employee {user_name} is done with tasks(
          {completed_tasks}/{total_tasks})")

    for todo in todo_data:
        if todo.get('completed'):
            print(f"\t{todo.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    todo_progress(employee_id)
