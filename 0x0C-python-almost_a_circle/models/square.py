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
        self.width = height
        self.height = height

    def update(self, *args, **kwargs):
        """ Update de propertys """
        lista = ['id', 'height', 'x', 'y']
        if args is None or len(args) is 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for x in range(0, len(args)):
                setattr(self, lista[x], args[x])

    def to_dictionary(self):
        """ to dictionari dict """
        dic = {}
        lista = ['id', 'size', 'x', 'y']
        for x in lista:
            dic[x] = getattr(self, x)
        return dic
