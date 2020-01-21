#!/usr/bin/python3
"""
Open a json file
"""
import json


def load_from_json_file(filename):
    """
    Load from JSON file to object python
    """
    with open(filename, mode="r+") as f:
        return json.load(f)
