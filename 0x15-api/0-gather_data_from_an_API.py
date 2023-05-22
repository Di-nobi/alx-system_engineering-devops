#!/usr/bin/python3
""" A python script for API """
import sys
import requests
if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    req = requests.get(url).json
    name = req.get("name")

    url_2 = 'https://jsonplaceholder.typicode.com/todos'
    req2 = requests.get(url_2).json()
    task_num = 0
    filed_task = []
    completed_tasks = 0

    for task in req2:
        if task.get('userId') == int(sys.argv[1]):
            task_num += 1
        if task.get("completed_tasks") is True:
            completed_tasks += 1
            filed_task.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(name, completed_tasks, task_num))

    for i in filed_tasks:
        print("\t {}".format(i))
