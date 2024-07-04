#!/usr/bin/python3
"""
function that queries the 'Reddit API' and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    number of subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "MyBot/1.0"}  # avoid Too Many Requests error
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()["data"]
        return data["subscribers"]
    else:
        return 0


if __name__ == "__main__":
    subreddit = "python"  # Change this to the subreddit you want to test
    subscribers = number_of_subscribers(subreddit)
    print(subscribers)

