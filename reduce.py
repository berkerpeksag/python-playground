#!/usr/bin/env python
# coding: utf-8

def add(x, y):
    return x + y

if __name__ == '__main__':
    lst = [1, 2, 3]

    sum_list = reduce(add, lst)
    print sum_list
  