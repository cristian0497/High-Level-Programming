#!/usr/bin/python3
def remove_char_at(str, n):
    cont = 0
    for char in str:
        if cont != n:
            print("{}".format(char), end="")
        cont += 1
    return ""
