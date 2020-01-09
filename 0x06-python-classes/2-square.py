#!/usr/bin/python3
"""
Module Class
"""


class Square:
    """
    Class Square
    """
    def __init__(self, size=0):
        """
        def __init__
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
