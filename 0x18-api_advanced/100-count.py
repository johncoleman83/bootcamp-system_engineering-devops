#!/usr/bin/python3
"""
queries to https://www.reddit.com/dev/api/
"""
import requests


def make_get_request(subreddit, after):
    """
    makes reddit get request to hot topics of subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if after:
        payload = {'after': after, 'limit': '100'}
    else:
        payload = {'limit': '100'}
    header = {'user-agent': 'one-dope-boy', 'over18': 'yes'}
    response = requests.get(
        url, headers=header, params=payload, allow_redirects=False
    )
    return response


def search_for_words(children, word_list):
    """
    searches for words in response
    """
    for child in children:
        title = child.get('data').get('title').lower()
        title_words = [word for word in title.split()]
        for word in word_list:
            count = title_words.count(word)
            if count > 0:
                word_list[word] += count
    return word_list


def print_results(word_list):
    """
    prints result list
    """
    word_list = [
        [word, count] for word, count in word_list.items() if count > 0
    ]
    word_list = sorted(word_list, key=lambda x: x[1], reverse=True)
    for word in word_list:
        print('{}: {}'.format(word[0], word[1]))


def count_words(subreddit, word_list, after=None):
    """
    prints the count of top ten hot posts for subreddit
    """
    if type(word_list).__name__ == 'list':
        word_list = {word.lower(): 0 for word in word_list}
    response = make_get_request(subreddit, after)
    if response.status_code == 200:
        data = response.json().get('data')
        after = data.get('after')
        children = data.get('children')
        word_list = search_for_words(children, word_list)
        if after:
            count_words(subreddit, word_list, after)
        else:
            print_results(word_list)
