#!/usr/bin/python3
"""
Method, add __repr__ method call
"""


class Rectangle:
    """
    Class Rectangle, print the area, perimeter, rectangle, add __repr__
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        string = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for x in range(self.__height):
            for y in range(self.__width):
                string += '#'
            string += '\n'
        return string[:-1]

    def __repr__(self):
        return("Rectangle ({}, {})".format(self.__width, self.__height))

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0:
            return 0
        if self.__width == 0:
            return 0
        per = (self.__height * 2) + (self.__width * 2)
        return per

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
