#!/usr/bin/python3
""" """
import requests
from sys import argv


if __name__ == "__main__":
    try:
        resps = requests.get("https://api.github.com/user",
                           auth=(argv[1], argv[2])).json()
        print(resps.get("id"))
    except:
        print("Not a valid PARAMETER")
