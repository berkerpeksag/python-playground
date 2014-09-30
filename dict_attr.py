from __future__ import print_function


class Dict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


if __name__ == '__main__':
    d = {'a': 'A', 'b': 'B'}
    e = Dict(d)
    print(e.a)
    e.c = 'C'
    print(e.c)
