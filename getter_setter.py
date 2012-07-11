#!/usr/bin/env python

class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

if __name__ == '__main__':
    c = C()
    print c.x
    c.x = 'Hodo'
    print c.x
