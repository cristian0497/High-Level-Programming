#!/usr/bin/python3
""" Method to request a Info GitHub API """
import requests
import sys


def main():
    """ Request the info from GITHUB API """
    usr = sys.argv[1]
    pwd = sys.argv[2]
    url = requests.get('https://api.github.com/user', auth = (usr, pwd))
    dic = url.json()
    print(dic.get("id"))

if __name__ == "__main__":
    main()
