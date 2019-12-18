#!/usr/bin/python3
def max_integer(my_list=[]):
    ref = 0
    idx = 0
    cont = 0
    for integer in my_list:
        if integer > ref:
            ref = integer
            idx = cont
        cont += 1
    return my_list[idx]
