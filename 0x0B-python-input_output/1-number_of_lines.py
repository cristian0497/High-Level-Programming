#!/usr/bin/python3
"""
Number of lines in the string
"""


def number_of_lines(filename=""):
    """
    Method to count the num of lines of a file
    """
    num = 0
    with open(filename) as f:
        for line in f:
            num += 1
    return num
