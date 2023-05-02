#!/usr/bin/python3
""" """
from sys import argv
from urllib import request, parse


if __name__ == "__main__":
    email = parse.urlencode({"email": argv[2]}).encode()
    reqst = request.Request(argv[1], email)
    with request.urlopen(reqst) as resp:
        print(resp.read().decode("utf8"))
