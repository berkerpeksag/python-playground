"""
Definition of even and odd for non-negative integers:

* a number is even if it is one more than an odd number
* a number is odd if it is one more than an even number
* 0 is even
"""


def debug(*msg):
    print(' -> ', *msg)


def is_even(n):
    debug('is_even()')
    debug('n =', n)
    if n == 0:
        debug('n == 0')
        return True
    else:
        debug('n-1 =', n-1)
        return is_odd(n-1)


def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n-1)


def is_even_inlined(n):
    if n == 0:
        return True
    else:
        if (n-1) == 0:
            return False
        else:
            return is_even((n-1)-1)

if __name__ == '__main__':
    print(is_even(4))
    print(is_even(7))
    print(is_even_inlined(4))
    print(is_even_inlined(7))
