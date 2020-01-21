#!/usr/bin/python3
"""
Append in a file
"""


def append_write(filename="", text=""):
    """
    Append to a file, create if dosnt exist
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
