#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a my_list.
    Args:
        my_list (list): The list of elements
        x (int): The number of elements to be printed.
    Returns:
        The number of elements that have been printed
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
