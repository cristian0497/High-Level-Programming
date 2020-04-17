#!/usr/bin/python3
""" Request package library """
import requests
import sys


def main():
    """ print the code error mesagge, or body of response """
    url = requests.get(sys.argv[1])
    if (url.status_code > 400):
        print("Error code: {}".format(url.status_code))
    else:
        print(url.text)

if __name__ == "__main__":
    main()
