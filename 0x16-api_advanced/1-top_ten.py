#!/usr/bin/python3
"""Prints hot posts"""


import requests


def top_ten(subreddit):
    """Prints titles of top 10"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    addHeaders = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
            }

    number = {
            "limit": 10
            }
    response = requests.get(url, headers=addHeaders,
                            params=number, allow_redirects=False)
    statusCode = response.status_code
    if statusCode == 404:
        print("None")
        return
    data = response.json().get("data")
    [print(i.get("data").get("title")) for i in data.get("children")]
