#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new = a_dictionary
    if key not in a_dictionary:
        return a_dictionary
    del new[key]
    return new
