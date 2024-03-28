#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL &
displays the value of the X-Request-Id variable,
found in the header of the response."""


from urllib.request import urlopen
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urlopen(url) as response:
        request_id = response.getheader('X-Request-Id')

    print(request_id)
