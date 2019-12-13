#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def main():
    if len(sys.argv) == 4:
        a, b = int(sys.argv[1]), int(sys.argv[3])
        sig = sys.argv[2]
        if sig == '+':
            print("{} {} {} = {}".format(a, sig, b,  add(a, b)))
        elif sig == '-':
            print("{} {} {} = {}".format(a, sig, b,  sub(a, b)))
        elif sig == '*':
            print("{} {} {} = {}".format(a, sig, b,  mul(a, b)))
        elif sig == '/':
            print("{} {} {} = {}".format(a, sig, b,  div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

if __name__ == "__main__":
    main()
