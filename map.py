#!/usr/bin/env python
# coding: utf-8

"""The map function takes a function and a number of
lists as arguments (usually just one) and applies the
function to each element of the list, collecting the
elements together into a new list.
"""

def add(x, y):
    return x + y

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]

    lists_sum = map(add, list1, list2)
    print lists_sum