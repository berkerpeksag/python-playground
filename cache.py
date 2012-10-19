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
"""

class Cache(object):

    def __init__(self, maxsize=100):
        self.cache = {}
        self.order = []  # least recently used first
        self.maxsize = maxsize

    def get(self, key):
        item = self.cache[key]  # KeyError if not present
        self.order.remove(key)
        self.order.append(key)
        return item

    def set(self, key, value):
        if self.cache.has_key(key):
            self.order.remove(key)
        elif len(self.cache) >= self.maxsize:
            # discard least recently used item
            del self.cache[self.order.pop(0)]
        self.cache[key] = value
        self.order.append(key)

    def size(self):
        return len(self.cache)
