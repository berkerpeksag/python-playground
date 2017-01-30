def debug(*msg):
    print(' -> ', *msg)


def sum_digits(n):
    """Return the sum of the digits of positive integer n."""
    debug('n =', n)
    if n < 10:
        debug('return', n)
        return n
    else:
        all_but_last, last = n // 10, n % 10
        debug('all_but_last =', all_but_last)
        debug('last =', last)
        return sum_digits(all_but_last) + last

if __name__ == '__main__':
    print(sum_digits(123))
