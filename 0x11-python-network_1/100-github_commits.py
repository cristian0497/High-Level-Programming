#!/usr/bin/python3
""" GitHub Request commits"""
import sys
import requests


def main():
    """ Github Request """
    st = "{}/{}".format(sys.argv[2], sys.argv[1])
    url = requests.get('https://api.github.com/repos/{}/commits'.format(st))
    response = url.json()
    for key in response[:10]:
        print("{}: {}".format(key['sha'], key['commit']['author']['name']))

if __name__ == "__main__":
    main()
