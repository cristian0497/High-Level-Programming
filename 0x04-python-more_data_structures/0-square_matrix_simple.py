#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [[x*x for x in line] for line in matrix]
    return new
