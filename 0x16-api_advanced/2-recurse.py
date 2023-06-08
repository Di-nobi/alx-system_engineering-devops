#!/usr/bin/python3
""" A recursive function that queries the API and returns a list
containing the titles of all hot articles for a subreddit"""

import requests
def recurse(subreddit, hot_list=[], after=None):
    """ A recursive function that queries the API """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Dinobis alx project'}
    params = {"after": after, "limit": 100}
    req = requests.get(url, headers=headers, params=params, allow_redirect=False)
    # prints (req, hot_list and after)
    if req.status_code != 200:
        return None
    find = req.json().get('data').get('children')
    hot_list = []

    for usr in find:
        hot_list.append(usr['data']['title'])

    after = req.json()['data']['after']
    if after is None:
        return hot_list
    else:
        recurse(subreddit, hot_list, after)
