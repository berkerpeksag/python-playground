#!/usr/bin/env python3

"""
The Algorithm Design Manual by Steven S. Skiena

1-28. [5] Write a function to perform integer division without using
either the / or + operators. Find a first way to do it.
"""

from __future__ import print_function


def divide(numerator, denominator):
    quotient = 0
    while numerator >= denominator:
        numerator -= denominator
        quotient += 1
    return quotient


if __name__ == '__main__':
    print(divide(4, 2))
    print(divide(6, 3))
    print(divide(10, 5))
    print(divide(50, 10))
