#!/usr/bin/env python
# coding: utf-8


def factorial(n, f=1):
    if n == 0:
        return f
    else:
        return factorial(n - 1, n * f)


def main():
    print factorial(5)
    print factorial(1)
    print factorial(0)
    print factorial(10)

if __name__ == '__main__':
    main()
