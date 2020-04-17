#!/usr/bin/python3
""" Request method package """
import requests


def main():
    """ request packager and print status and type of responde """
    url = requests.get('https://w3schools.com/python/demopage.htm')
    print("Body responde:")
    print("\t- type: {}".format(type(url.text)))
    print("\t- content: {}".format(url.reason))

if __name__ == "__main__":
    main()
