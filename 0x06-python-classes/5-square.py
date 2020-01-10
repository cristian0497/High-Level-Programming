#!/usr/bin/python3
"""
Module
"""


class Square:
    def __init__(self, size=0):
        """
        init and check the values to object code
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size

    def area(self):
        """
        return: Area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with size
        """
        if self.__size == 0:
            print()
            return
        for j in range(self.__size):
            for i in range(self.__size):
                print("#", end="")
            print()

    @property
    def size(self):
        """
        the property of the object
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        call to setter
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value
