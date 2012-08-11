#!/usr/bin/env python
# coding: utf-8

import sys

PY3 = sys.version_info[0] == 3


def py2_unicode(klass):
    if not PY3:
        klass.__unicode__ = klass.__str__
        klass.__str__ = lambda self: self.__unicode__().encode('utf-8')
    return klass


@py2_unicode
class A(object):
    def __str__(self):
        return 'foo bar'

if __name__ == '__main__':
    a = A()
    print a
