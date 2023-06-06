#!/usr/bin/python3
"""
A function that queries the API and returns the number of subscribers 
"""
import requests

def def number_of_subscribers(subreddit):
    """ Gets number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    req = requests.get(url)
    if req.json().get('data').get('subscribers')  is None:
        return 0
