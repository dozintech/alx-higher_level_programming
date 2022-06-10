#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    '''
    Prints a dictionary's contents with the keys in a sorted order

    Parameters:
    a_dictionary (dict): A dictionary
    '''
    for key in sorted(a_dictionary.keys()):
        print('{:s}: {}'.format(key, a_dictionary[key]))
