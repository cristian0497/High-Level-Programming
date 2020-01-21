#!/usr/bin/python3
"""
Open and read file
"""


def read_file(filename=""):
    """
    Read File...
    """
    with open(filename) as f:
        for line in f:
            print(line, end="")
