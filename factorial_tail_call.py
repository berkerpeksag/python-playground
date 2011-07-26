#!/usr/bin/env python
# coding: utf-8

def factorial(n, f = 1):
    if n == 0:
        return f
    else:
        return factorial(n - 1, n * f)

if __name__ == '__main__':
    print factorial(5)
  