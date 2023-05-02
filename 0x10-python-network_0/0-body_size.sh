#!/bin/bash
# Takes in a URL and sends a req
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
