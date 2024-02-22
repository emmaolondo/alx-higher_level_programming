#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
displays the value of the X-Request-Id variable found in the
header of the response.
"""


import urllib.request
import sys

if __name__ == "__main__":
    # check if a url is provided
    if len(sys.argv) != 2:
        print("./script.py <URL>")
        sys.exit(1)

    url = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(url) as response:
        header = response.getheader('X-Request-Id')
        print(header)
