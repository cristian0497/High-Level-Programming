#!/usr/bin/python3


class Square:
    """ Class Square """
    def __init__(self, size=0):
        """ Initialize self"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Return the Area """
        return (self.__size ** 2)
