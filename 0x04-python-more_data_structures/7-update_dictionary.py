#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    '''
    Replaces or adds key/value in a dictionary

    Parameters:
    a_dictionary (dict): The dictionary to modify
    key (str): The key to add
    value (Any): The value of the key

    Returns:
    The modified dictionary
    '''
    a_dictionary[key] = value
    return a_dictionary
