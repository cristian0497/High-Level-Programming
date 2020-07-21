#!/usr/bin/python3

for cont in range(122, 96, -1):
    if cont % 2 == 1:
        cont = cont - 32
    print("{:c}".format(cont), end="")
