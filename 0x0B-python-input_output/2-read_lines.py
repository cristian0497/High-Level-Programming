#!/usr/bin/python3
"""
Read N lines of a file
"""


def read_lines(filename="", nb_lines=0):
    """
    Print N llines method
    """
    with open(filename) as f:
        for x in range(nb_lines):
            print(f.readline(), end="")
        if nb_lines <= 0:
            for line in f:
                print(line, end="")
