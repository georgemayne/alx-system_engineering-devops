#!/usr/bin/python3
"""
the number of subscribers (not active users, total subscribers)
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns
    the number of subscribers (not active users,
    total subscribers) for a given subreddit.
    """
    if not isinstance(subreddit, str):
        return (0)

    user_agent = {
        'User-agent': (
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
            '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )
    }

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        response = requests.get(url, headers=user_agent)
        response.raise_for_status()

        # Check if the subreddit exists
        if response.status_code == 404:
            print(f"Subreddit '{subreddit}' does not exist.")
            return (0)

        results = response.json()
        return results.get('data', {}).get('subscribers', 0)

    except requests.exceptions.RequestException as req_exc:
        print(f'Request error occurred: {req_exc}')
        return (0)
