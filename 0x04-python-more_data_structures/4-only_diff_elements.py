#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    '''
    Creates a set consisting of elements that are not intersecting
    the two given sets

    Parameters:
    set_1 (set): The first set
    set_2 (set): The second set

    Returns:
    A set containing items that can be found in only one of the two given sets
    '''
    new_set_list = []
    new_set_list.extend(set_1)
    new_set_list.extend(set_2)
    new_set_list = filter(
        lambda item: not (item in set_1 and item in set_2),
        new_set_list
    )
    return set(new_set_list)
