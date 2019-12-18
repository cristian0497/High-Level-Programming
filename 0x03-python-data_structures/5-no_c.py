#!/bin/usr/python3
def no_c(my_string):
    st = ''
    for char in my_string:
        if char is not 'cC':
            st = ''.join(char)
    return (st)
