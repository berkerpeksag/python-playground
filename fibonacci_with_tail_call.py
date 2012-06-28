#!/usr/bin/env python
# coding: utf-8


def fibonacci(n, current=0, next=1):
    if n == 0:
        return current
    else:
        print 'fibonacci(%d - 1, %d, %d + %d)' % (n - 1, next, current, next)
        return fibonacci(n - 1, next, current + next)


def main():
    print fibonacci(5)
    print fibonacci(1)
    print fibonacci(0)
    print fibonacci(10)
    print fibonacci(3)

if __name__ == '__main__':
    main()
