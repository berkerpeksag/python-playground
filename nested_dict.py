# coding: utf-8


class NestedDict(dict):
    def __getitem__(self, key):
        if key in self:
            return self.get(key)
        return self.setdefault(key, NestedDict())

    def __add__(self, other):
        return other

    def __sub__(self, other):
        return other


def main():
    d = NestedDict()
    d['a']['b'] = 'c'
    print d


if __name__ == '__main__':
    main()
