#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    x = 0
    y = 0
    while x < len(matrix):
        while y < len(matrix[x]):
            print("{:d}".format(matrix[x][y]), end="")
            y += 1
        print('\n', end="")
        x += 1
        y = 0
