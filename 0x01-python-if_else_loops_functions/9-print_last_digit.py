#!/usr/bin/python3
def print_last_digit(number):
    number_conv = 0
    if number < 0:
        number_conv = number * -1
    elif number > 0:
        number_conv = number
    num = number_conv % 10
    print(num, end="")
    return num
