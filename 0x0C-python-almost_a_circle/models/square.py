#!/usr/bin/python3
"""
Class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.height))

    @property
    def size(self):
        """ Getter size"""
        return self.height

    @size.setter
    def size(self, height):
        """ Setter of size"""
        self.height = height
        self.width = height
