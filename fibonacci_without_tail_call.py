#!/usr/bin/env python
# coding: utf-8

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    print fibonacci(100)