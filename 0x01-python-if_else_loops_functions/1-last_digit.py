#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number_conv = number * -1
elif number > 0:
    number_conv = number
num = number_conv % 10
txt = "Last digit of "
if num > 5:
    print(txt + "{} is {} and is greater than 5".format(number, num))
elif num == 0:
    print(txt + "{} is {} and is 0".format(number, num))
elif num < 6:
    print(txt + "{} is {} and is less than 6 and not 0".format(number, num))
