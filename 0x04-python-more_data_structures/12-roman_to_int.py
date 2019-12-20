#!/usr/bin/pthon3
def roman_to_int(roman_string):
    ret = 0
    valores = {
        'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10,
        'V': 5, 'I': 1}
    if len(roman_string) == 0:
        return None
    for i in roman_string:
        if i in valores:
            ret += valores[i]
    return ret
