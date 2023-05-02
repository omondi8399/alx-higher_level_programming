#!/usr/bin/python3
""" """
import requests
from sys import argv


if __name__ == "__main__":
    resps = requests.get(argv[1])
    print(resps.headers.get('X-Request-Id'))
