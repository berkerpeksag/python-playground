"""
There is one fundamental difference between Singleton and Borg: Borg are
different objects with shared state and Singleton are one object.

Notes
-----

Classes and modules are singletons. You don't need singletons in python simply
because classes and modules are always singletons, and they are also first
class objects. They can have everything instances have, and as import
statements don't make copies there is only ever one of them. We don't need no
stinkin' design patterns.

http://code.activestate.com/recipes/66531-singleton-we-dont-need-no-stinkin-singleton-the-bo/#c23
"""

from __future__ import print_function


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if '_instance' not in cls.__dict__:
            cls._instance = object.__new__(cls, args, kwargs)
        return cls._instance


class Borg(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        self = object.__new__(cls, *args, **kwargs)
        self.__dict__ = cls._state
        return self


def borg(cls):
    """A class decorator for Borg design pattern."""
    cls._state = {}
    _new = cls.__new__

    def wrapper(self, *args, **kwargs):
        self.__dict__ = cls._state
        _new(self, *args, **kwargs)

    cls.__new__ = wrapper
    return cls


@borg
class Spam(object):
    def eggs(self):
        print('Borg!')
