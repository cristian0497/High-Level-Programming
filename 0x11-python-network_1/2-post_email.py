#!/usr/bin/python3
""" Method to request URL """
import urllib.request
import sys


def main():
    """ method to send information """
    url = sys.argv[1]
    data = {"email": sys.argv[2]}

    request = urllib.parse.urlencode(data)
    request = request.encode('ascii')
    req = urllib.request.Request(url, request)
    with urllib.request.urlopen(req) as response:
        print("{}".format(response.read().decode('utf-8')))

if __name__ == "__main__":
    main()
