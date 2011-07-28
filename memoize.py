#!/usr/bin/env python
# coding: utf-8

def memoize(function):
    cache = {}

    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            val = function(*args)
            cache[args] = val

            return val

    return decorated_function