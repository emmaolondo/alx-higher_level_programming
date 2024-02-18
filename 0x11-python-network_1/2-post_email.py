#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter
displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    # check if a url and an email are provided
    if len(sys.argv) != 3:
        print("./script.py <url> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    values ={'email' : email}
    data = urllib.parse.urlencode(values).encode('ascii')
    fetch = urllib.request.Request(url, data)
    with urllib.request.urlopen(fetch) as response:
        html = response.read().decode("utf-8")
        print(html)
