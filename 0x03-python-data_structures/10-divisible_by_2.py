#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    tmp = my_list[:]
    cont = 0
    for integer in my_list:
        if integer % 2 == 0:
            tmp[cont] = True
        elif integer % 2 == 1:
            tmp[cont] = False
        cont += 1
    return tmp if tmp else my_list
