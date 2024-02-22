#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL
displays the body of the response (decoded in utf-8).

You have to manage urllib.error.HTTPError exceptions
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("./script.py <URL>")
        sys.exit(1)

    url = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            print(html)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
