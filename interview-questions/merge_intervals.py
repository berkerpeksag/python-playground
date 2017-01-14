"""
Complexity

- O(n log n) for sorted()
- O(n) for the merging

= O(n log n)

O(1) space

"""

import operator
import unittest


def merge_intervals(intervals):
    if not intervals:
        return

    sorted_intervals = sorted(intervals, key=operator.itemgetter(0))
    low, high = sorted_intervals[0]

    for i in sorted_intervals[1:]:
        if i[0] <= high:
            high = max(high, i[1])
        else:
            yield low, high
            low, high = i

    yield low, high


class MergeIntervalsTestCase(unittest.TestCase):

    def test_merge_intervals(self):
        tests = [
            ([], []),
            ([(0, 2)], [(0, 2)]),
            ([(0, 3), (1, 2)], [(0, 3)]),
            ([(5, 7), (11, 116), (3, 6), (10, 12), (6, 12)], [(3, 116)]),
            ([(1, 3), (2, 6), (8, 10), (15, 18)], [(1, 6), (8, 10), (15, 18)]),
            ([(6, 8), (1, 9), (2, 4), (4, 7)], [(1, 9)]),
            ([(1, 6), (2, 3), (4, 5)], [(1, 6)]),
        ]
        for intervals, expected in tests:
            with self.subTest(intervals=intervals):
                self.assertEqual(list(merge_intervals(intervals)), expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
