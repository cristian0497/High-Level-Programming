#!/usr/bin/python3
""" JSON post response query"""
import sys
import requests


def main():
    """ POST request and print the return with JSON values """
    dic = {}
    dic['q'] = sys.argv[1] if (len(sys.argv) > 1) else ""
    try:
        url = requests.post('http://0.0.0.0:5000/search_user', data=dic)
        response = url.json()
        if (response):
            id_user = response.get("id")
            name = response.get("name")
            print("[{}] {}".format(id_user, name))
        else:
            print("No result")
    except:
        print("Not a valid JSON")

if __name__ == "__main__":
    main()
