#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as err_msg:
        print("Exception: " + str(err_msg), file=sys.stderr)
        return False
