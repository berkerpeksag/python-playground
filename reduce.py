#!/usr/bin/env python
# coding: utf-8

"""You can use reduce to reduce a list to a single value
by applying a function to the first two elements, then
apply the same function to the result of the first function
call and the next element, etc. until all the elements
have been processed.
"""


def add(x, y):
    return x + y


def main():
    l = [1, 2, 3]

    sum_list = reduce(add, l)
    print sum_list

if __name__ == '__main__':
    main()
