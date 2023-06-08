#!/usr/bin/python3
""" A function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit """
import requests

def top_ten(subreddit):
    """ Top ten hot posts """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    req = requests.get(url, headers={'User-Agent': 'Dinobi User 1.0'})

    if req.status_code != 200:
        print(None)
        return
    usr_list = req.json().get('data').get('children')
    for usr in usr_list:
        print(usr.get('data').get('title'))
