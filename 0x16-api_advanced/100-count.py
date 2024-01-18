#!/usr/bin/python3
"""Queries Reddit API to determine subreddit sub count
"""
import requests


def count_words(subreddit, word_list, count_list=[], after=None):
    '''Prints counts of given words recursively.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        count_list (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
    '''
    user_agent = {'User-agent': '0x16-api_advanced-Osaclay'}
    posts = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                         .format(subreddit, after), headers=user_agent)
    if after is None:
        word_list = [word.lower() for word in word_list]

    if posts.status_code == 200:
        posts = posts.json()['data']
        aft = posts['after']
        posts = posts['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    count_list.append(word)
        if aft is not None:
            count_words(subreddit, word_list, count_list, aft)
        else:
            result = {}
            for word in count_list:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(result.items(), key=lambda item: item[1],
                                     reverse=True):
                print('{}: {}'.format(key, value))
    else:
        return

