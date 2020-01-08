#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ret = []
    for i in range(list_length):
        try:
            ret.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            ret.append(0)
        except TypeError:
            print("wrong type")
            ret.append(0)
        except IndexError:
            print("wrong type")
            ret.append(0)
    return ret
