#!/usr/bin/python3
""" request package for python """
import requests
import sys


def main():
    """ print the Request ID """
    url = requests.get(sys.argv[1])
    print(url.headers['X-Request-Id'])

if __name__ == "__main__":
    main()
