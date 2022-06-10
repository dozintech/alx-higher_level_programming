#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
    Computes the square of a 2D list of integers
    Parameters:
    matrix (list): The 2D list of integers
    Returns:
    A new 2D list of integers with the integers squared or None
    '''
    if matrix is None:
        return None
    new_matrix = []
    for row in matrix:
        new_row = []
        for col in row:
            new_row.append(col ** 2)
        new_matrix.append(new_row)
    return new_matrix
