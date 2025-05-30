#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            printed = printed + 1
        except (TypeError, ValueError):
            continue
    print()
    return printed
