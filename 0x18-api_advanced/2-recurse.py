#!/usr/bin/python3
"""
queries to https://www.reddit.com/dev/api/
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns the top ten hot posts for subreddit
    """
    domain = 'https://www.reddit.com'
    path = '/r/{}/hot.json'.format(subreddit)
    url = '{}{}'.format(domain, path)
    if after:
        payload = {
            'after': after,
            'count': str(len(hot_list)),
            'limit': str(100)
        }
    else:
        payload = {
            'limit': str(100)
        }
    header = {
        'user-agent': 'one-dope-boy',
        'over18': 'yes'
    }
    response = requests.get(
        url,
        headers=header,
        params=payload,
        allow_redirects=False
    )
    code = response.status_code
    if code >= 300:
        return None
    data = response.json().get('data')
    after = data.get('after')
    children = data.get('children')
    for child in children:
        hot_post = child.get('data')
        title = hot_post.get('title')
        hot_list.append(title)
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
