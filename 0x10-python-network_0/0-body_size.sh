#!/bin/bash
# Bash script that takes a URL, sends request and displays size of body of the response
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
