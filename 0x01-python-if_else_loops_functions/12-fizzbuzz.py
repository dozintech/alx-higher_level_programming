#!/usr/bin/python3
def fizzbuzz():
    '''
    Prints the numbers from 1 to 100 separated by a space
    but for multiples of 3 prints 'Fizz' and multiple of
    5 prints 'Buzz'
    '''
    for i in range(1, 101):
        print('{:s}{:s}{:s}'.format(
            str(i) * ((i % 3 != 0) and (i % 5 != 0)),
            'Fizz' * (i % 3 == 0),
            'Buzz' * (i % 5 == 0),
        ), end=' ')
