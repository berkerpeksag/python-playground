#!/usr/bin/env python
# coding: utf-8

def fibonacci(n, current = 0, next = 1):
    if n == 0:
        return current
    else:
        return fibonacci(n - 1, next, current + next)

if __name__ == '__main__':
    print fibonacci(100)