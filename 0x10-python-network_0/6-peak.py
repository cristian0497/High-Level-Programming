#!/usr/bin/python3
""" A peak into a unsorted numbers """


def find_peak(list_int):
    if len(list_int) > 0:
        y = 1
        for x in range(0, len(list_int)):
            if list_int[x] >= list_int[x-1] and list_int[x] >= list_int[x + 1]:
                return list_int[x]
        if list_int[y] > list_int[y + 1]:
            return list_int[y]
        else:
            return list_int
