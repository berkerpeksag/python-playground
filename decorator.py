from __future__ import print_function


# This is a higher-order function.
def trace(fn):
    def wrapped(x):
        print('->', fn, x)
        return fn(x)
    return wrapped


@trace
def triple(x):
    return 3 * x

if __name__ == '__main__':
    for i in range(5):
        print(i, triple(i))
