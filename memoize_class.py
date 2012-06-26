#!/usr/bin/env python
# coding: utf-8

class cached_property(object):
    """A memoize decorator for class properties."""

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, type):
        result = instance.__dict__[self.func.__name__] = self.func(instance)
        return result


class Test(object):
    """A test class."""

    @cached_property
    def hede(self):
        return 'Hede'
