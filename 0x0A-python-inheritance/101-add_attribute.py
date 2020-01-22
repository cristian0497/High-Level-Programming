#!/usr/bin/python3
"""
Set attribute
"""


def add_attribute(obj, at_name, attribute):
    """
    Set attribute in a object specified
    """
    if hasattr(obj, at_name):
        raise TypeError("can't add new attribute")
    obj.__setattr__(at_name, attribute)
