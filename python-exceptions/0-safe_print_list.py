#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    for element in range(x):
        try:
            print("{}".format(my_list[element]), end="")
            printed = printed + 1
        except IndexError:
            break
    print()
    return printed
