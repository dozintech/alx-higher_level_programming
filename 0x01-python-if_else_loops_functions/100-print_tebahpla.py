#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    print('{:c}'.format(i - ((i % 2) * (1 << 5))), end='')
