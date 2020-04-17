#!/usr/bin/python3
""" GitHub Request commits"""
import sys
import requests


def main():
    """ Github Request """
    st = "{}/{}".format(sys.argv[1], sys.argv[2])
    url = requests.get('https://api.github.com/repos/{}/commits'.format(st))
    response = url.json()
    for x in response[:10]:
        print("{}: {}".format(x['sha'], x['author']['login']))

if __name__ == "__main__":
    main()
