#!/usr/bin/python3
"""
 a Python script that takes in a URL, sends a request to the URL
 displays the value of the variable X-Request-Id in the\
         response header
You must use the packages requests and sys
"""
import requests, sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    url = sys.argv[1]

    response = requests.get(url)
    header = response.headers.get("X-Request-Id")
    print(header)
