def uniq_add(my_list=[]):
    new = []
    for num in my_list:
        if num not in new:
            new.append(num)
    ret = sum(new)
    return ret
