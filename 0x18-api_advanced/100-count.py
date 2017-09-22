#!/usr/bin/python3
"""
queries to https://www.reddit.com/dev/api/
"""
import requests


def count_words(subreddit, word_list, after=None):
    """
    returns the top ten hot posts for subreddit
    """
    if type(word_list).__name__ == 'list':
        word_list = {
            word: 0 for word in word_list
        }
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
    code = response.status_code
    if code >= 300:
        return
    data = response.json().get('data')
    after = data.get('after')
    children = data.get('children')
    for child in children:
        hot_post = child.get('data')
        title = hot_post.get('title').split()
        for word in word_list:
            word_list[word] += title.count(word)
    if after:
        return count_words(subreddit, word_list, after)
    else:
        words_counts = [
            (word, count) for word, count in word_list.items() if count > 0
        ]
        words_counts = sorted(words_counts, key=lambda x: x[1])
        for word in words_counts:
            print('{}: {}'.format(word[0], word[1]))
        return
