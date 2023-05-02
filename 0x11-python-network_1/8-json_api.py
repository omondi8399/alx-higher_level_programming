#!/usr/bin/python3
""" """

import requests
from sys import argv


if __name__ == "__main__":
    param = ""
    if len(argv) == 2:
        param = argv[1]
    try:
        res = requests.post("http://0.0.0.0:5000/search_user",
                            data={'q': param}).json()
        if ("id" in res) and ("name" in res):
            print("[{}] {}".format(res['id'], res['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
