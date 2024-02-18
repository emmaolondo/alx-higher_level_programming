#!/usr/bin/python3
""" post an email using the requests package """


import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    info = {'email': email}
    response = requests.post(url, data=info)
    print(response.text)
