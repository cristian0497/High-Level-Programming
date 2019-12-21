#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) > 0:
        x = sum([a * b for a, b in my_list])
        y = sum([b for a, b in my_list])
    return x / y
