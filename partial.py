from __future__ import print_function

import functools


def add(x, y):
    return x + y


if __name__ == '__main__':

    add5_partial = functools.partial(add, 5)
    print(add5_partial(10))  # 15

    add5_lambda = lambda x: add(x, 5)
    print(add5_lambda(10))  # 15
