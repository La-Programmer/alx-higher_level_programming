#!/bin/bash
# Script to return the size of the response
if [ $# -lt 1 ]; then
    echo "IP address / URL required"
    exit 1
fi
curl -s -w "%{size_download}\n" -o /dev/null "$1"
