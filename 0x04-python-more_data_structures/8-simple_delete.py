#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    '''
    Deletes a key in a dictionary

    Parameters:
    a_dictionary (dict): The dictionary to modify
    key (str): The key to delete

    Returns:
    The modified dictionary
    '''
    if key in a_dictionary.keys():
        a_dictionary.pop(key)
    return a_dictionary
