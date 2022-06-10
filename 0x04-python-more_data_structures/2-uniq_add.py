#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''
    Adds all unique integers in a list

    Parameters:
    my_list (list): The list of integers

    Returns:
    A sum of the unique integers in the given list
    '''
    res = 0
    for num in set(my_list):
        res += num
    return res
