#!/usr/bin/python3
"""a function that queries the Reddit API
and returns the number of subscribers
(not active users, total subscribers)
for a given subreddit."""


import requests


def number_of_subscribers(subreddit):
    """Returns number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    addHeaders = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
            }
    response = requests.get(url, headers=addHeaders, allow_redirects=False)

    statusCode = response.status_code
    if statusCode == 404:
        return 0
    data = response.json().get("data")
    return data.get("subscribers")
