#!/usr/bin/env python
# coding: utf-8

def fibonacci(n):
    a, b = 0, 1 # a = 0 and b = 1

    while a < n:
        print a,

        a, b = b, a + b # a = b and b = a + b

if __name__ == '__main__':
    fibonacci(100)
