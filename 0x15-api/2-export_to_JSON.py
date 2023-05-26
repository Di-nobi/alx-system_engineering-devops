#!/usr/bin/python3
""" Exports file to json """
import json
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    req = requests.get(url)
    username = req.json().get("username")

    url2 = 'https://jsonplaceholder.typicode.com/todos'
    req2 = requests.get(url2)
    data = {sys.argv[1] : []}

    for item in req2.json():
        if item.get("userId") == int(sys.argv[1]):
            data[sys.argv[1]].append({'task': item.get('title'), 'completed':
                                     item.get('completed'), 'username': username})
    files = sys.argv[1] + '.json'
    with open(files, 'w') as f:
        json.dump(data, f)
