#!/usr/bin/python3
"""
Load, Add and save
"""
import sys


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = 'add_item.json'

if __name__ == "__main__":
    try:
        data = load_from_json_file(filename)
    except:
        data = []
    for x in range(1, len(sys.argv)):
        data.append(sys.argv[x])
    save_to_json_file(data, filename)
