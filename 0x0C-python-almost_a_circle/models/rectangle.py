#!/usr/bin/python3
"""
Class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.x, self.y,
                                                        self.width,
                                                        self.height))

    @property
    def width(self):
        """ Property of width """
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ Property of height """
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ property of x """
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ property of y """
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ Area of rectangle """
        return (self.__height * self.__width)

    def display(self):
        """ print the Rectangule  width, height, x, y, id"""
        for y in range(0, self.__y):
            print()
        for line in range(0, self.__height):
            for x in range(0, self.x):
                print(" ", end="")
            for colum in range(0, self.__width):
                print("#", end="")
            print()

    def update(self, *args):
        try:
            self.id = args[0]
        except:
            pass
        try:
            self.width = args[1]
        except:
            pass
        try:
            self.height = args[2]
        except:
            pass
        try:
            self.x = args[3]
        except:
            pass
        try:
            self.y = args[4]
        except:
            pass
