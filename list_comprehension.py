#!/usr/bin/env python
# coding: utf-8


def main():
    foo = [x for x in xrange(1, 11) if not x % 2]  # or just range(2, 11, 2)
    print foo

if __name__ == '__main__':
    main()
