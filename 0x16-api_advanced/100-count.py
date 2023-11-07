#!/usr/bin/python3
""", and prints a sorted count of given keywords"""


import requests


def count_words(subreddit, word_list, dicts={}, newElem="", count=0):
    """prints a sorted count of given keywords"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
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

    try:
        data = response.json()
        statusCode = response.status_code
        if statusCode == 404:
            raise Exception
    except Exception:
        print("")
        return

    data = data.get("data")
    newElem = data.get("after")
    count += data.get("dist")

    for child in data.get("children"):
        label = child.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in label:
                number = len([s for s in label if s == word.lower()])
                if dicts.get(word) is None:
                    dicts[word] = number
                else:
                    dicts[word] += number

    if newElem is None:
        if len(dicts) == 0:
            print("")
            return
        dicts = sorted(dicts.items(), key=lambda kv: (-kv[1], kv[0]))
        [print(f"{k}: {v}") for k, v in dicts]
    else:
        count_words(subreddit, word_list, dicts, newElem, count)
