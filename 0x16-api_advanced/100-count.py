#!/usr/bin/python3
"""100-count
"""
import json
from operator import itemgetter

import requests

BASE_URL = "https://www.reddit.com/r"
HEADERS = {"User-Agent": "ALX-Bot"}


def count_words(subreddit, word_list, after=None, counter=None):
    """recursively calls the reddit api to get list hot posts and count the
    given keyword in their title

    Args:
        subreddit (str): title of the subreddit
        word_list (list): list of key words
        after (str, optional): id of the hot posts list. Defaults to None.
        counter (list, optional): KeyWord list counter. Defaults to None.
    """
    if len(word_list) == 0:
        return

    if counter is None:
        counter = {}
        for word in word_list:
            if word.lower() not in counter:
                counter[word.lower()] = 0

    query = "" if after is None else "&after={}".format(after)
    result = requests.get(
        "{}/{}/hot.json?limit=100{}".format(BASE_URL, subreddit, query),
        headers=HEADERS,
        allow_redirects=False,
    )

    if result.status_code == 200:
        data = json.loads(result.text)["data"]

        for post in data["children"]:
            title = post.get('data').get("title").lower().split()
            for word in word_list:
                counter[word.lower()] += sum(w == word.lower() for w in title)

        after = data["after"]
        if after is None:
            counter = sorted(
                sorted(counter.items()),
                key=itemgetter(1),
                reverse=True,
            )
            for word in counter:
                if word[1] > 0:
                    print("{}: {}".format(word[0], word[1]))
        else:
            count_words(subreddit, word_list, after, counter)