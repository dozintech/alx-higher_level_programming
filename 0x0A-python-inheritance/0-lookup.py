#!/usr/bin/python3
'''A module for inspecting an object.
'''


def lookup(obj):
    '''Finds the list of available attributes and methods of an object.

    Args:
        obj (any): A given object.

    Returns:
        list: A list of available attributes and methods the object has.
    '''
    return dir(obj)
