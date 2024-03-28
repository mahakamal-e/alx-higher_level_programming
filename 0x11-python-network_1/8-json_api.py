#!/usr/bin/python3
""" takes a letter and sends a POST request to URL with letter as a parameter"""


import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    response = requests.post(url, data={'q': letter})
    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response.get("id"),
                                   json_response.get("name")))
        else:
            print("No result")
    except ValueError:
         print("Not a valid JSON")
