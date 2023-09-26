#!/usr/bin/python3
"""Using rest api"""


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
        name = datas.get("name")

        lists = requests.get(person)
        list_data = lists.json()

        completed = [task for task in list_data if task["completed"]]
        totals = len(list_data)
        count = len(completed)

        print(f"Employees {name} is done with tasks ({count}/{totals}):")
        for task in completed:
            print(f"\t{task['title']}")
    except Exception as e:
        sys.exit(1)


if len(sys.argv) != 2:
    sys.exit(1)
get_employee(int(sys.argv[1]))
