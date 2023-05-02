#!/usr/bin/python3
""" """
import requests
from sys import argv


if __name__ == "__main__":
    try:
        resps = requests.get(argv[1])
        resps.raise_for_status()
        print(resps.text)
    except:
        print("Error code: {}".format(resps.status_code))
