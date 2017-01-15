"""
Simple cache implementation
---------------------------

The following is a simple cache implementation, which is suitable for relatively
small caches (up to a few hundred items), and where it’s relatively costly to
create or reload objects after a cache miss (e.g. a few milliseconds or more per
object).

Usage::

    cache = Cache()

    try:
        item = cache.get(key)
    except KeyError:
        item = item_factory()
        cache.set(key, item)

    print(len(cache))
"""

import unittest


class Cache:

    def __init__(self, *, maxsize=100):
        self.cache = {}
        self.order = []  # least recently used first
        self.maxsize = maxsize

    def get(self, key):
        item = self.cache[key]  # KeyError if not present
        self.order.remove(key)
        self.order.append(key)
        return item

    def set(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.maxsize:
            # discard least recently used item
            del self.cache[self.order.pop(0)]
        self.cache[key] = value
        self.order.append(key)

    def __len__(self):
        return len(self.cache)


class CacheTestCase(unittest.TestCase):

    def setUp(self):
        self.cache = Cache()

    def test_get(self):
        self.assertRaises(KeyError, self.cache.get, 'foo')
        self.cache.set('foo', 'bar')
        self.assertEqual(self.cache.get('foo'), 'bar')

    def test_set(self):
        self.cache.set('foo', 'foo')
        self.assertEqual(self.cache.get('foo'), 'foo')
        self.cache.set('foo', 'bar')
        self.assertEqual(self.cache.get('foo'), 'bar')

    def test_len(self):
        self.assertEqual(len(self.cache), 0)
        self.cache.set('bar', 'baz')
        self.assertEqual(len(self.cache), 1)
        self.cache.set('key', 'value')
        self.assertEqual(len(self.cache), 2)

    def test_maxsize(self):
        self.assertEqual(self.cache.maxsize, 100)
        cache = Cache(maxsize=42)
        self.assertEqual(cache.maxsize, 42)

if __name__ == '__main__':
    unittest.main(verbosity=2)
