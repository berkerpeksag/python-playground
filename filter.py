#!/usr/bin/env python
# coding: utf-8

"""You can use filter to create a list which contains
a subset of the elements of an input list.
"""


def is_odd(n):
    return n % 2 == 1


def main():
    nums = xrange(1, 101)

    odd_nums = filter(is_odd, nums)
    print odd_nums

if __name__ == '__main__':
    main()
