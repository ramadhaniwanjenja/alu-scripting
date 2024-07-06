#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a given subreddit.
    If the subreddit is invalid, return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "MyBot/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    print("Status Code:", response.status_code)  # Debugging line
    if response.status_code == 200:
        data = response.json()
        print("Response JSON:", data)  # Debugging line
        return data.get("data", {}).get("subscribers", 0)
    return 0
