#!/usr/bin/python3
def safe_print_division(a, b):
    '''
    Safely prints the quotient of two integers

    Parameters:
    a (int): The first integer
    b (int): The second integer

    Returns:
    The quotient of the two integers, otherwise None
    '''
    res = 0
    try:
        res = a / b
    except Exception:
        res = None
    finally:
        print("Inside result: {}".format(res))
    return res
