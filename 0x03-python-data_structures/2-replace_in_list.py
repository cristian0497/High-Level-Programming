#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx >= 0:
        cont = 0
        for integer in my_list:
            if idx == cont:
                my_list[cont] = element
                return my_list
            cont += 1
    return my_list
