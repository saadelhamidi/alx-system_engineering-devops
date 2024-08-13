#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests

def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if not subreddit or not isinstance(subreddit, str):
        return 0
    
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError if the response was unsuccessful
        data = response.json()
        subs = data.get("data", {}).get("subscribers", 0)
        return subs
    except (requests.RequestException, ValueError) as e:
        # Log or handle the error as needed
        print(f"Error: {e}")
        return 0
