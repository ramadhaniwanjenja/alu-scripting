#!/usr/bin/python3
"""Return the number of subscribers for a given subreddit"""
import requests

def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Will raise an HTTPError for bad responses (4xx and 5xx)
        data = response.json()
        
        # Extracting the number of subscribers
        subscribers = data.get('data', {}).get('subscribers', 0)
        return subscribers
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0

