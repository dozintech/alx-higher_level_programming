#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    '''
    Creates a new dictionary with all values in a given
    dictionary multiplied by 2

    Parameters:
    a_dictionary (dict): The source dictionary

    Returns:
    A new dictionary consisting of value of the given
    dictionary multiplied by 2
    '''
    if a_dictionary is None:
        return None
    new_dict = dict()
    for key in a_dictionary.keys():
        new_dict[key] = a_dictionary[key] * 2
    return new_dict
