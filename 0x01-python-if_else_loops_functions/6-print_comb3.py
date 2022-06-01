#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j:
            print('{:d}{:d}{:s}'.format(
                i, j, '\n' if (i == 8) and (j == 9) else ', '), end='')
