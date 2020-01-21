#!/usr/bin/python3
"""
"""
import json


def class_to_json(obj):
    """
    take a object to convert in a dictionary representation
    """
    object_dic = {}
    object_dic.update(obj.__dict__)
    return object_dic
