#!/usr/bin/python3
def no_c(my_string):
    st = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            st += ''.join(char)
    return (st)
