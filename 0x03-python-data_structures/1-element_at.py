#!/usr/bin/python3
def element_at(my_list, idx):
    if idx >= 0:
        cont = 0
        for integer in my_list:
            if idx == cont:
                return my_list[idx]
            cont += 1
    return none
