#!/usr/bin/python3
"""
queries to https://www.reddit.com/dev/api/
"""
import requests


def make_get_request(subreddit, after, hot_list):
    """
    makes get request to reddit API
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if after:
        payload = {
            'after': after, 'count': str(len(hot_list)), 'limit': '100'
        }
    else:
        payload = {'limit': '100'}
    header = {
        'user-agent': 'one-dope-boy',
        'over18': 'yes'
    }
    response = requests.get(
        url, headers=header,
        params=payload, allow_redirects=False
    )
    return response


def add_titles(hot_list, children):
    """
    adds new titles to hottlist
    """
    for child in children:
        hot_post = child.get('data')
        title = hot_post.get('title')
        hot_list.append(title)
    return hot_list


def recurse(subreddit, hot_list=[], after=None):
    """
    returns the top ten hot posts for subreddit
    """
    response = make_get_request(subreddit, after, hot_list)
    code = response.status_code
    if code >= 300:
        return None
    data = response.json().get('data')
    after = data.get('after')
    children = data.get('children')
    hot_list = add_titles(hot_list, children)
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
