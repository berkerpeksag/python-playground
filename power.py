# coding: utf-8

"""
This simple algorithm illustrates an important principle of divide and conquer.
It always pays to divide a job as evenly as possible. This principle applies to
real life as well.

When `n` is not power of two, the problem cannot always be divided perfect
evenly, but a difference of one element between the two sides cannot cause any
serious imbalance

Algorithm Design Manual, Chapter 2: Algorithm Analysis, 2.6.5 Fast Exponention
"""

import unittest


def power(a, n):
    if n == 0:
        return 1
    divide = power(a, n / 2)
    if n % 2 == 0:
        return divide ** 2
    else:
        return a * divide ** 2


class TestPower(unittest.TestCase):
    def test_power(self):
        self.assertEqual(4, power(2, 2))
        self.assertEqual(2, power(2, 1))
        self.assertEqual(8, power(2, 3))
        self.assertEqual(104857600000000000000000000L, power(20, 20))

if __name__ == '__main__':
    unittest.main()
