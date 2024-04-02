#!/bin/bash
# Print the body of a response with header code 200
if [ "$(curl -s -w "%{http_code}\n" -o /dev/null "$1")" -eq 200 ]; then curl -s "$1"; fi
