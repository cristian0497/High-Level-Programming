#!/usr/bin/python3
"""
Base Geometry
"""


class BaseGeometry:
    """
    Class BaseGeometry
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Class Rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
