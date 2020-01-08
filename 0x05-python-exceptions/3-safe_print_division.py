#!/usr/bin/python3
def safe_print_division(a, b):
    ret = 0
    print("Inside result: ", end="")
    try:
        ret = a / b
    except:
        ret = None
    finally:
        print("{}".format(ret))
    return ret
