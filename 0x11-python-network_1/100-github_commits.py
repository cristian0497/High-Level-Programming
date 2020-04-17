#!/usr/bin/python3
""" GitHub Request commits"""
import sys
import requests


def main():
    """ Github Request """
    dic = {}
    dic['author'] = sys.argv[2]
    dic['repo'] = sys.argv[1]
    url = requests.get('https://api.github.com/repos/', params=dic)
    response = url.json()
    print(response)

if __name__ == "__main__":
    main()
