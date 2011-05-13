#!/usr/bin/env python
# coding: utf-8

"""
To master yield, you must understand that when you call the function, the code you have written in the function body does not run. The function only returns the generator object, this is bit tricky.
"""

def create_generator():
    for i in range(3):
        yield i * i

if __name__ == '__main__':
    my_generator = create_generator()

    print my_generator

    for i in my_generator:
        print i
