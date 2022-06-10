#!/usr/bin/python3
def common_elements(set_1, set_2):
    '''
    Creates a set consisting of items common to two given sets

    Parameters:
    set_1 (set): The first set
    set_2 (set): The second set

    Returns:
    A set containing items that can be found in the two sets
    '''
    new_set_list = []
    for item in set_1:
        if item in set_2:
            new_set_list.append(item)
    return set(new_set_list)
