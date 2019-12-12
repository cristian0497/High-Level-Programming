#!/usr/bin/python3
import sys


def main():
    n = len(sys.argv)
    cont = 1
    print("{:d} argument".format(n - 1) + ("." if n == 2 else "s"), end="")
    print(":" if n > 2 else "")
    while cont < n:
        if n > 1:
            print("{:d}: {}".format(cont, sys.argv[cont]))
        cont += 1
if __name__ == "__main__":
    main()
