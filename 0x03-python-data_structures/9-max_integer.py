#!/usr/bin/python3
def max_integer(my_list=[]):
    ref = 0
    idx = 0
    cont = 0
    if len(my_list) == 0:
        return None
    for integer in my_list:
        if integer > ref:
            ref = integer
            idx = cont
        cont += 1
    return my_list[idx]
