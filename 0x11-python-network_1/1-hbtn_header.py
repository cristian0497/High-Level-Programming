#!/usr/bin/python3
""" methon to request header"""
import urllib.request
import sys


def main():
    """ function to print the request id """
    url = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(url) as response:
        info = response.headers.get("X-Request-Id")
        print(info)

if __name__ == "__main__":
    main()
