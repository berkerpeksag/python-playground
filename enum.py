"""Simple and incomplete enum implementations in Python."""

from __future__ import print_function
from collections import namedtuple


class Enum(set):

    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError


class Enum2(tuple):
    __getattr__ = tuple.index


def enum(*keys):
    return namedtuple('Enum', keys)(*range(len(keys)))

if __name__ == '__main__':
    Animals = Enum(['DOG', 'CAT', 'HORSE'])
    print(Animals.DOG)

    Animals2 = Enum2(['DOG', 'CAT', 'HORSE'])
    print(Animals2.DOG)

    Animals3 = enum('DOG', 'CAT', 'HORSE')
    print(Animals3.DOG)
