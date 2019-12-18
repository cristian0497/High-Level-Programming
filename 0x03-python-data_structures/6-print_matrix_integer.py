#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for midx in matrix:
        if not midx:
            print("")
        x = 0
        for integer in midx:
            print("{:d}".format(integer), end="")
            print(" " if x < len(midx) - 1 else '\n', end="")
            x += 1
