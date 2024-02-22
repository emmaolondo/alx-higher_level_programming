#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status
"""


import urllib.request

if __name__ == "__main__":
    """
    fetch a url and display the body of the response
    """
    fetch = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(fetch) as response:
        html = response.read()
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- utf8 content:", html.decode('utf-8'))
