#!/bin/bash
# Script to return the size of the response
curl -s -w "%{size_download}\n" -o /dev/null "$1"
