#!/usr/bin/env python
# coding: utf-8


def factorial(n):
    r = 1

    for i in reversed(range(1, n + 1)):
        r *= i

    return r


def main():
    print factorial(5)
    print factorial(1)
    print factorial(0)
    print factorial(10)
    print factorial(-3)

if __name__ == '__main__':
    main()
