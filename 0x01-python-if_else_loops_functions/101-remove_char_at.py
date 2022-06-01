#!/usr/bin/python3
def remove_char_at(str, n):
    '''
    Creates a new string with the character at the given index removed
    Parameters:
    str (str): The source string
    n (int): The 0-based index of the character to remove
    '''
    new_str = []
    for i in range(len(str)):
        if i != n:
            new_str.append(str[i])
    return ''.join(new_str)
