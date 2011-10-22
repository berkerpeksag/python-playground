#!/usr/bin/env python
# coding: utf-8


class A(object):
    def __getattribute__(self, name):
        if name.startswith('print_'):
            return object.__getattribute__(self, name[6:])

        return object.__getattribute__(self, name)

    def hi(self):
        print 'Hello!'

a = A()

a.hi()
a.print_hi()
