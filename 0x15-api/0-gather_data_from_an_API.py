#!/usr/bin/python3
""" A python script for API """
import requests
import sys
if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    req = requests.get(url)
    name = req.json().get("name")

    url_2 = 'https://jsonplaceholder.typicode.com/todos'
    req2 = requests.get(url_2)
    task_num = 0
    filed_task = []
    completed_tasks = 0

    for task in req2.json():
        if task.get('userId') == int(sys.argv[1]):
            task_num += 1
            if task.get("completed") is True:
                completed_tasks += 1
                filed_task.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          completed_tasks,
                                                          task_num))

    for i in filed_task:
        print("\t {}".format(i))
