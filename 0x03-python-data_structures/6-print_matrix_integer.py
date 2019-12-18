#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    x = 0
    y = 0
    lenx = len(matrix)
    if lenx == 1:
        print("")
    leny = len(matrix[x])
    while x < lenx:
        while y < leny:
            print("{}".format(matrix[x][y]), end="")
            print(" " if y < leny - 1 else '\n', end="")
            y += 1
        y = 0
        x += 1
