#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    '''
    Prints the elements of a list

    Parameters:
    my_list (list): The list containing the elements to be printed
    x (int): The number of elements to print

    Returns:
    The actual number of elements printed
    '''
    n = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            n += 1
        except Exception:
            break
    print("")
    return n
