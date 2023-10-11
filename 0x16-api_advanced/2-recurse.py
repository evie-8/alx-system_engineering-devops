#!/usr/bin/python3
"""a list
containing the titles
of all hot articles for a given subreddit"""


import requests


def recurse(subreddit, hot_list=[], newElem="", count=0):
    """the titles of all hot articles for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    addHeaders = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
            }

    newParams = {
            "after": newElem,
            "count": count,
            "limit": 100
            }

    response = requests.get(url, headers=addHeaders,
                            params=newParams,
                            allow_redirects=False)

    statusCode = response.status_code
    if statusCode == 404:
        return None

    data = response.json().get("data")
    newElem = data.get("after")
    count += data.get("dist")
    for child in data.get("children"):
        hot_list.append(child.get("data").get("title"))

    if newElem is not None:
        return recurse(subreddit, hot_list, newElem, count)
    return hot_list
