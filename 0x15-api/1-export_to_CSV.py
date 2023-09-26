#!/usr/bin/python3
"""Using rest api"""


import csv
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
        ids = datas.get("id")

        lists = requests.get(person)
        list_data = lists.json()

        completed = [task for task in list_data if task["completed"]]
        totals = len(list_data)
        count = len(completed)

        files = f"{ids}.csv"
        with open(files, "w", newline="") as f:
            csv_writer = csv.writer(f,  quoting=csv.QUOTE_ALL)
            for task in completed:
                csv_writer.writerow([ids, name,
                                     task["completed"], task["title"]])
    except Exception as e:
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    get_employee(int(sys.argv[1]))
