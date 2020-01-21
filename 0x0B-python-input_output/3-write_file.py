#!/usr/bin/python3
"""
Write in file, overwrite if already exists
"""


def write_file(filename="", text=""):
    """
    Methon to open, write the file
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
