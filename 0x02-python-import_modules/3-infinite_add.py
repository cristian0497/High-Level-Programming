#!/usr/bin/python3
import sys


def main():
    cont, res = 1, 0
    n = len(sys.argv)
    if n > 1:
        while cont < n:
            res += int(sys.argv[cont])
            cont += 1
        print("{}".format(res))
    else:
        print(0)
if __name__ == "__main__":
    main()
