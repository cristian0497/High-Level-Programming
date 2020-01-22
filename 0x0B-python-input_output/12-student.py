#!/usr/bin/python3
"""
Return a student class dict
"""


class Student:
    """
    Class Student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (attrs is None) or (type(attrs) != list):
            return self.__dict__
        ret = {}
        for arg in attrs:
            for key in self.__dict__:
                if arg == key:
                    ret[key] = (self.__dict__[key])
        return ret
