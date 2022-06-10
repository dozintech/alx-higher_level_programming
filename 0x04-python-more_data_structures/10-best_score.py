#!/usr/bin/python3
def best_score(a_dictionary):
    '''
    Finds the key with the biggest integer value in a given dictionary

    Parameters:
    a_dictionary (dict): The source dictionary

    Returns:
    The key with the biggest integer value
    '''
    if a_dictionary is None or len(a_dictionary.keys()) == 0:
        return None
    best_score = 0
    res = ''
    i = 0
    for key in a_dictionary.keys():
        if a_dictionary[key] > best_score or i == 0:
            best_score = a_dictionary[key]
            res = key
        i += 1
    return res
