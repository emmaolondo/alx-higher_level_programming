#!/usr/bin/python3
"""
python script that lists 10 commits from the most recent\
        of the repository rails by the user rails
"""


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    repo = sys.argv[1]  # repository
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    req = requests.get(url)
    if req.status_code == 200:
        commits = req.json()
        for info in commits[:10]:
            sha = info['sha']
            author = info['commit']['author']['name']
            print(f"{sha}: {author}")
    else:
        print("None")
