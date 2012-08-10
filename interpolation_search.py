#!/usr/bin/env python
# coding: utf-8

"""
Interpolation search algorithm in Python

To run the benchmark::

    python -m timeit -v -s 'from interpolation_search import run; run(999999)'

http://en.wikipedia.org/wiki/Interpolation_search
"""

from sys import argv


def interpolation_search(sorted_list, to_find):
    low = 0
    high = len(sorted_list) - 1

    while sorted_list[low] <= to_find and sorted_list[high] >= to_find:
        mid = low + ((to_find - sorted_list[low]) * (high - low)) \
              / (sorted_list[high] - sorted_list[low])
              # out of range is possible

        if sorted_list[mid] < to_find:
            low = mid + 1
        elif sorted_list[mid] < to_find:
            high = mid - 1
        else:
            return mid

    if sorted_list[low] == to_find:
        return low
    return None


def run(find):
    sorted_list = sorted(range(10000000))
    search = interpolation_search(sorted_list, int(find))
    if search is None:
        return 'not found'
    else:
        return search

if __name__ == '__main__':
    if len(argv) == 2:
        print run(argv[1])
    else:
        exit('Usage: {0} [int]'.format(__file__))
