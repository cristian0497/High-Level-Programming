#!/usr/bin/python3
"""
inherit ftom int
"""


class MyInt(int):
    def __eq__(self, Num):
        return int(self) != int(Num)

    def __ne__(self, Num):
        return int(self) == int(Num)
