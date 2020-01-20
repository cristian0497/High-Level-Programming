#!/usr/bin/python3
"""
SubClass of list
"""

class MyList(list):
    """ Print sorted list """
    def print_sorted(self):
        print(sorted(self))
