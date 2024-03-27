#!/bin/bash
# Takes a URL, sends a POST request, displays the body of the response.
curl -s -X POST -d "email=$email&subject=$subject" "$1"
