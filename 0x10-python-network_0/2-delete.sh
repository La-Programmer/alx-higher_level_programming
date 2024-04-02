#!/bin/bash
# Sends a delete request using curl
echo $(curl -sX DELETE "$1")
