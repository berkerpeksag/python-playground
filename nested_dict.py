from __future__ import print_function


class NestedDict(dict):

    def __getitem__(self, key):
        if key in self:
            return self.get(key)
        return self.setdefault(key, NestedDict())


class NestedDictAlt(dict):

    def __missing__(self, key):
        return self.setdefault(key, NestedDictAlt())


if __name__ == '__main__':
    d = NestedDict()
    d['a']['b'] = 'c'
    print(d)

    d2 = NestedDictAlt()
    d2['a']['b'] = 'c'
    print(d2)
