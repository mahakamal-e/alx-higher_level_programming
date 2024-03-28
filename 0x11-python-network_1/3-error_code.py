#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL &
displays the body of the response (decoded in utf-8)."""


from urllib.request import urlopen
import sys
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urlopen(url) as response:
            body = response.read().decode("utf-8")
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
