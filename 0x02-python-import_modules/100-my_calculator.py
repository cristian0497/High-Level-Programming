#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def main():
    if len(sys.argv) == 4:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        sig = sys.argv[2]
        if sig == '+':
            ret = add(a, b)
        elif sig == '-':
            ret = sub(a, b)
        elif sig == '*':
            ret = mul(a, b)
        elif sig == '/':
            ret = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        print("{} {} {} = {:d}".format(a, sig, b,  ret))
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

if __name__ == "__main__":
    main()
