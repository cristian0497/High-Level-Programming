#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    tmp = {}
    for x in a_dictionary:
        tmp[x] = a_dictionary[x] * 2
    return tmp
