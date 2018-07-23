# Adapted from Lib/unittest/mock.py without pickle support.

class _SentinelObject:
    """A unique, named, sentinel object."""
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'sentinel.%s' % self.name


class _Sentinel:
    """Access attributes to return a named object, usable as a sentinel."""
    def __init__(self):
        self._sentinels = {}

    def __getattr__(self, name):
        return self._sentinels.setdefault(name, _SentinelObject(name))


sentinel = _Sentinel()

if __name__ == '__main__':
    default = sentinel.DEFAULT
    assert repr(default) == 'sentinel.DEFAULT'
    assert default == sentinel.DEFAULT
    assert default is sentinel.DEFAULT
    assert default != sentinel.FOO
