#!/usr/bin/python3
""" Request method package """
import requests


def main():
    """ request packager and print status and type of responde """
    url = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(url.text)))
    print("\t- content: {}".format(url.text))

if __name__ == "__main__":
    main()
