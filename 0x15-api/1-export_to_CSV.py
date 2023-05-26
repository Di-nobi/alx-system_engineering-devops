#!/usr/bin/python3
""" Exports data in the CSV format """
import csv
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    req = requests.get(url)
    userName = req.json().get("username")

    url2 = 'https://jsonplaceholder.typicode.com/todos'
    req2 = requests.get(url2)

    files = sys.argv[1] + '.csv'
    line = []
    for i in req2.json():
        if i.get("userId") == int(sys.argv[1]):
            line.append([i.get("userId"),
                userName, i.get("completed"), i.get("title")])

    with open(files, 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for r in line:
            writer.writerow(r)
