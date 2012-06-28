#!/usr/bin/env python
# coding: utf-8


def fibonacci(n):
    a, b = 0, 1  # a = 0 and b = 1

    while a < n:
        print a,

        a, b = b, a + b  # a = b and b = a + b


def main():
    print fibonacci(5)
    print fibonacci(1)
    print fibonacci(0)
    print fibonacci(10)
    print fibonacci(3)

if __name__ == '__main__':
    main()
