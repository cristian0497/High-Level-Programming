#!/usr/bin/python3
"""
matrix_divided - Return a list with div of elements
"""


def matrix_divided(matrix, div):
    """
    Return a new list with div function
    """
    new = []
    if matrix == [None] or None:
        raise TypeError('matrix must be a matrix '
                        '(list of lists) of integers/floats')
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if type(matrix) != list:
        raise TypeError('matrix must be a matrix '
                        '(list of lists) of integers/floats')

    for x in range(len(matrix)):
        try:
            _len = len(matrix[x + 1])
        except:
            _len = len(matrix[x])
        if len(matrix[x]) != _len:
            raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        n_row = []
        for num in row:
            if type(num) != int and type(num) != float:
                raise TypeError('matrix must be a matrix '
                                '(list of lists) of integers/floats')
            n_row.append(float("{0:.2f}".format(num / div)))
        new.append(n_row)
    return new
