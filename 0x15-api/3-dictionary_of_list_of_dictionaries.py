#!/usr/bin/python3
"""Using rest api"""


import json
import requests
import sys


def get_employee():
    """function to get id """
    url = "https://jsonplaceholder.typicode.com"
    user_url = f"{url}/users"

    try:
        data = requests.get(user_url)
        datas = data.json()

        all_people = {}
        for i in datas:
            ids = i.get("id")
            name = i.get("username")
            user = f"{url}/todos?userId={ids}"

            news = requests.get(user)
            lists = news.json()

            tasks = [
                    {
                        "username": name,
                        "task": task["title"],
                        "completed": task["completed"]
                        }
                    for task in lists
                    ]
            all_people[ids] = tasks
            files = "todo_all_employees.json"
            with open(files, "w") as f:
                json.dump(all_people, f)

    except Exception as e:
        sys.exit(1)


if __name__ == "__main__":
    get_employee()
