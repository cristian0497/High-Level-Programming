#!/usr/bin/python3
"""
Pascal triangle
"""


def pascal_triangle(size):
    """
    Pascal Triangle
    """
    if size <= 0:
        return []
    triangle = [[1], [1, 1]]
    for x in range(1, size):
        line = [1]
        for y in range(0, len(triangle[x]) - 1):
            line.extend([triangle[x][y] + triangle[x][y + 1]])
        line += [1]
        triangle.append(line)
    return triangle
