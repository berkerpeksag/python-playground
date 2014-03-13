from __future__ import print_function


def fac1(n):
    """Iterative factorial example."""
    r = 1
    for i in xrange(1, n + 1):
        r *= i
    return r


def fac2(n, f=1):
    """Tail recursive factorial example."""
    if n == 1:
        return f
    return fac2(n - 1, n * f)


if __name__ == '__main__':
    for fac in (fac1, fac2):
        print(fac.__doc__)
        print(fac(5))
        print(fac(1))
        print(fac(0))
        print(fac(7))
        print(fac(-3))
