#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''
    Replaces all occurrences of an element by another in a new list

    Parameters:
    my_list (list): The list of items
    search (Any): The item in the list to be replaced
    replace (Any): The item to use as a replacement

    Returns:
    A new list with the search item replaced with the replace item
    '''
    if my_list is None:
        return None
    new_list = []
    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list
