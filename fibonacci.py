from __future__ import print_function


def fib1(n):
    """Iterative fibonacci example."""
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


def fib2(n):
    """Recursive fibonacci example."""
    if n < 2:
        return n
    return fib2(n - 1) + fib2(n - 2)


def fib3(n, current=0, next_item=1):
    """Tail recursive fibonacci example."""
    if n == 0:
        return current
    return fib3(n - 1, next_item, current + next_item)


if __name__ == '__main__':
    for fib in (fib1, fib3, fib2):
        print(fib.__doc__)
        print(fib(5))
        print(fib(1))
        print(fib(0))
        print(fib(10))
        print(fib(3))
        print(fib(20))
        print(fib(100))
