#!/usr/bin/python3
import sys


def main():
    n = len(sys.argv) - 1
    cont = 0
    print("{:d} argument".format(n) + (":" if n == 1 else "s"), end="")
    if n == 0:
        print(".", end="")
    print(":" if n > 1 else "")
    while cont < n:
        if n > 0:
            print("{:d}: {}".format(cont + 1, sys.argv[cont + 1]))
        cont += 1
if __name__ == "__main__":
    main()
