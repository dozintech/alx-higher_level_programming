#!/usr/bin/python3
for i in range(100):
    print('{:02d}{:s}'.format(i, ', ' * (i < 99) + '\n' * (i == 99)), end='')
