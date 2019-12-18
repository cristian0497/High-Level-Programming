#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= 0:
        tmp = my_list[:]
        cont = 0
        for integer in my_list:
            if cont == idx:
                tmp[cont] = element
                return tmp
            cont += 1
    return my_list
