#!/usr/bin/python3
""" """
import urllib.request
from sys import argv


if __name__ == "__main__":
    reqst = urllib.request.Request(argv[1])
    with urllib.request.urlopen(reqst) as res:
        print(res.headers['X-Request-Id'])
