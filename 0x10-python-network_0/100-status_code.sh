#!/bin/bash
# Send request, passed as an argument & displays the status code of the response.
curl -sL -o /dev/null -w "%{http_code}" "$1"
