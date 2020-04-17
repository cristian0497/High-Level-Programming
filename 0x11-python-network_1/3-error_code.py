#!/usr/bin/python3
""" Method to request URL"""
import urllib.request
import sys


def main():
    """ Request and print error code, or body """
    url = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode())
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.status))

if __name__ == "__main__":
    main()
