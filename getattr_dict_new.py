#!/usr/bin/env python
# coding: utf-8


class A(object):
    def __getattr__(self, name):
        if name not in self.__dict__:
            object.__setattr__(self, name, None)

        return object.__getattribute__(self, name)

a = A()

print a.foo
a.foo = 42
print a.foo
a.bar = 'Hello!'
print a.bar
