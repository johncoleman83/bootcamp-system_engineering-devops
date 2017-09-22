#!/usr/bin/python3
"""
queries to https://www.reddit.com/dev/api/
"""
import requests


def make_get_request(subreddit, after):
    """
    makes reddit get request to hot topics of subreddit
    """
    domain = 'https://www.reddit.com'
    path = '/r/{}/hot.json'.format(subreddit)
    url = '{}{}'.format(domain, path)
    if after:
        payload = {
            'after': after,
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
    return response


def print_results(word_list):
    """
    prints result list
    """
    word_list = sorted(
        list(word_list),
        key=lambda x: x[1],
        reverse=True
    )
    found = None
    for word in word_list:
        if word[1] > 0:
            found = True
            print('{}: {}'.format(word[0], word[1]))
    if not found:
        print()


def search_for_words(children, word_list):
    """
    searches for words in response
    """
    for child in children:
        hot_post = child.get('data')
        title = hot_post.get('title')
        title_words = [word.lower() for word in title.split()]
        for word in word_list:
            word[1] += title_words.count(word[0].lower())
    return word_list


def count_words(subreddit, word_list, after=None):
    """
    prints the count of top ten hot posts for subreddit
    """
    if type(word_list).__name__ == 'list':
        word_list = tuple(
            [word, 0] for word in word_list
        )
    response = make_get_request(subreddit, after)
    code = response.status_code
    if code > 200:
        # print()
        return
    data = response.json().get('data')
    after = data.get('after')
    children = data.get('children')
    word_list = search_for_words(children, word_list)
    if after:
        count_words(subreddit, word_list, after)
    else:
        print_results(word_list)
