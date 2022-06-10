#!/usr/bin/python3
def number_keys(a_dictionary):
    '''
    Computes the number of keys in a dictionary

    Parameters:
    a_dictionary (dict): A dictionary

    Returns:
    The number of keys in the given dictionary
    '''
    if a_dictionary is not None:
        return len(a_dictionary.keys())
    else:
        return 0
