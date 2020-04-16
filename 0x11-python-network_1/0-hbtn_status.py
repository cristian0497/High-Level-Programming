#!/usr/bin/python3
""" Status of a web Page """
import urllib.request


if __name__ == "__main__":
    """ request a urllib """
    url = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(url) as response:
        info = response.read()
        print("Body response:")
        print("\t - type: {}".format(type(response.read())))
        print("\t - content: {}".format(info))
        print("\t - utf8 content: {}".format(info.decode('utf-8')))
