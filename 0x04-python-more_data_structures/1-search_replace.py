#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cont = 0
    tmp = my_list[:]
    if not tmp:
        return my_list
    for x in my_list:
        tmp[cont] = x
        if cont == search - 1:
            tmp[cont] = replace
        cont += 1
    return tmp
