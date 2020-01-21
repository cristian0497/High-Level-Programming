#!/usr/bin/python3
"""
object python represented by a JSON
"""
import json


def from_json_string(my_str):
    """
    method to JSON to object python
    """
    return json.loads(my_str)
