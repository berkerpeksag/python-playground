from __future__ import print_function


class ClassAttr(object):

    def __init__(self, value=None):
        self.value = value

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self.value
        raise AttributeError('instance var')


class Spam(object):
    x = ClassAttr(10)


if __name__ == '__main__':
    s = Spam()
    print(Spam.x)
    print(s.x)
