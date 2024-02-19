#!/usr/bin/python3
"""
 Python script that takes your GitHub credentials (username and password)
 and uses the GitHub API to display your id
"""


import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"
    if len(sys.argv) != 3:
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]

    req = requests.get(url, auth=(username, password))
    if req.status_code == 200:
        print(req.json().get('id'))
    else:
        print("None status code: {}".format(req.status_code))
