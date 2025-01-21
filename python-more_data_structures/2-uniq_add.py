#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = list(dict.fromkeys(my_list))
    total = sum(new_list)
    return total
