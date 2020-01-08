#!/usr/bin/python3
def safe_print_division(a, b):
    ret = 0
    try:
        print("Inside result:", end="")
        ret = a / b
    except:
        return None
    finally:
        print("{}".format(ret))
    return ret
