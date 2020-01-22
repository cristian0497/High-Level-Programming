#!/usr/bin/python3
"""
Add a string if string in file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Append a string into a file
    """
    ret = []
    with open(filename, mode="r+") as f:
        for line in f:
            ret.append(line)
            if search_string in line:
                ret.append(new_string)
        f.write("".join(ret))
