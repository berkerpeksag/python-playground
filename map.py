#!/usr/bin/env python
# coding: utf-8

def add(x, y):
    return x + y

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]

    lists_sum = map(add, list1, list2)
    print lists_sum