#!/usr/bin/python3
""" Takes a URL, sends a request &
displays the value of the variable X-Request-Id"""


import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    response = request.get(url)
    header = response.headers.get("X-Request-Id")
    print(header)
