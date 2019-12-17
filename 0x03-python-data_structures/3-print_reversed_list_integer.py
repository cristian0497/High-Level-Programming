#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    cont = len(my_list)
    if cont > 0 and my_list is not None:
        for integer in my_list:
            print("{:d}".format(my_list[cont - 1]))
            cont -= 1
