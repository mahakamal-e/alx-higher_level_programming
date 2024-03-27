#!/bin/bash
# Send request, passed as an argument & displays the status code of the response.
curl -sLw "%{http_code}" -o /dev/null "$1"
