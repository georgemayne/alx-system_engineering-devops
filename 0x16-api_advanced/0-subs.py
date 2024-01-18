#!/usr/bin/python3
"""Queries Reddit API to get subreddit sub count
"""

import requests


def number_of_subscribers(subreddit):
    """Request number of subscribers of subreddit
    from Reddit API
    """
    # set custom user-agent
    user_agent = '0x16-api_advanced-Osaclay'
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)

    # custom user-agent avoids request limit
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return 0

    # load response unit from json
    data = r.json()['data']
    # extract list of pages
    pages = data['children']
    # extract data from first page
    page_data = pages[0]['data']
    # return number of subreddit subs
    return page_data['subreddit_subscribers']

