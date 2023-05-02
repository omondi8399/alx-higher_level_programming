#!/usr/bin/python3
""" """
import requests


if __name__ == "__main__":
    resps = requests.get('https://intranet.hbtn.io/status').text
    print("Body response:")
    print("\t- type: {}".format(type(resps)))
    print("\t- content: {}".format(resps))
