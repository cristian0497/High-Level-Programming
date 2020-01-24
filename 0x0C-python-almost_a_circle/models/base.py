#!/usr/bin/python3
"""
Class base
"""
import json


class Base:
    """
    Class Base change id()
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ dictionary python to Json string """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save into a file json """
        filename = (cls.__name__ + ".json")
        with open(filename, mode="w") as f:
            lis = []
            if list_objs is None:
                f.write(cls.to_json_string(lis))
            else:
                for it in range(0, len(list_objs)):
                    lis.append(list_objs[it].to_dictionary())
                f.write(cls.to_json_string(lis))
