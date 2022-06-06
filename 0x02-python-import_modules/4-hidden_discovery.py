#!/usr/bin/python3
if __name__ == '__main__':
    from importlib import import_module
    hidden_4 = import_module('hidden_4')
    for name in sorted(dir(hidden_4)):
        if name[0:2] != '__':
            print('{:s}'.format(name))
