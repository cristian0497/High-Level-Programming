#!/usr/bin/python3
""" Request package for python """
import requests
import sys


def main():
    """ request and send a dictionary, print the request """
    obj = {"email" : sys.argv[2]}
    url = requests.post(sys.argv[1], data = obj)
    print(url.text)

if __name__ == "__main__":
    main()
