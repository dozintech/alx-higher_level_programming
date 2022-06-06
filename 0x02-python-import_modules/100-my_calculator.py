#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) == 4:
        funcs = [('+', add), ('-', sub), ('*', mul), ('/', div)]
        for func in funcs:
            if sys.argv[2] == func[0]:
                a = int(sys.argv[1])
                b = int(sys.argv[3])
                print('{:d} {:s} {:d} = {:d}'.format(
                    a, func[0], b, func[1](a, b)
                    ))
                sys.exit()
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
    else:
        print('Usage: {:s} <a> <operator> <b>'.format(sys.argv[0]))
        sys.exit(1)
