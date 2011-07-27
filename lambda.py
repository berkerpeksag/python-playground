#!/usr/bin/env python
# coding: utf-8

"""A lambda statement represents an anonymous function.
See map.py, reduce.py and filter.py
"""

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]

    # map.py
    list_map = map(lambda x, y: x + y, list1, list2)

    # reduce.py
    list_reduce = reduce(lambda x, y: x + y, list1)

    # filter.py
    nums = xrange(101)
    odd_nums = filter(lambda x: x % 2 == 1, nums)

    print 'Map', list_map
    print 'Reduce', list_reduce
    print 'Filter', odd_nums
  