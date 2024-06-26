#!/usr/bin/python3
'''
function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
'''
import requests


def number_of_subscribers(subreddit):
    '''Return the total number of subscribers on a given subreddit.'''

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, allow_redirects=False)

    if response.status_code != 200:
        return 0
    results = response.json().get('data')
    return results.get("subscribers")
