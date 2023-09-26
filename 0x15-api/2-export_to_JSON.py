#!/usr/bin/python3
"""Using rest api"""


import json
import requests
import sys


def get_employee(job_id):
    """function to get id """
    url = "https://jsonplaceholder.typicode.com"
    job_url = f"{url}/users/{job_id}"
    person = f"{url}/todos?userId={job_id}"

    try:
        data = requests.get(job_url)
        datas = data.json()
        name = datas.get("username")
        ids = datas.get("id")

        lists = requests.get(person)
        list_data = lists.json()

        completed = [task for task in list_data]
        totals = len(list_data)
        count = len(completed)
        dicts = {f"{job_id}": [{"task": task["title"],
                               "completed": task["completed"],
                                "username": name}
                               for task in list_data]}

        files = f"{ids}.json"
        with open(files, "w") as f:
            json.dump(dicts, f)

    except Exception as e:
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    get_employee(int(sys.argv[1]))
