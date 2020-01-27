#!/usr/bin/python3
"""
Class base
"""
import json
import os
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """ load from json """
        if json_string is None or len(json_string) is 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Return a instance with all attr """
        if cls.__name__ == "Square":
            ret = cls(2)
        else:
            ret = cls(2, 2)
        ret.update(**dictionary)
        return ret

    @classmethod
    def load_from_file(cls):
        """ returt a list of instances """
        list_ret = []
        filename = cls.__name__ + ".json"
        print(filename)
        if os.path.exists(filename) is False:
            return list_ret
        with open(filename, mode="r") as f:
            line = f.read()
        n_line = cls.from_json_string(line)
        for x in range(0, len(n_line)):
            list_ret.append(cls.create(**n_line[x]))
        return list_ret
"""
    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w") as data:
            data_csv = csv.writer(data,
            if cls.__name__ == "Rectangle":
    @classmethod
    def load_from_file_csv(cls):
"""
