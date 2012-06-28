#!/usr/bin/env python
# coding: utf-8

from memoize import memoize


@memoize
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    print fibonacci(5)
    print fibonacci(1)
    print fibonacci(0)
    print fibonacci(10)
    print fibonacci(3)

if __name__ == '__main__':
    main()
