from __future__ import print_function


class RevealAccess(object):
    """A data descriptor that sets and returns values
    normally and prints a message logging their access."""

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Retrieving', self.name)
        print(obj, objtype)
        return self.val

    def __set__(self, obj, val):
        print ('Updating', self.name)
        self.val = val


class MyClass(object):
    x = RevealAccess(10, 'x')
    y = 5


class prop(object):
    """Emulate @property."""

    def __init__(self, get_func):
        self.get_func = get_func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.get_func(instance)

    def __set__(self, instance, value):
        self.set_func(instance, value)

    def setter(self, set_func):
        self.set_func = set_func
        return self

    def set_func(self, instance, value):
        raise TypeError("can't set me")


class Demo(object):

    def __init__(self, i):
        self.i = i

    @prop
    def square(self):
        return self.i ** 2

    @square.setter
    def square(self, value):
        self.i = value

    @prop
    def normalize(self):
        return '[%i]' % self.i


if __name__ == '__main__':
    a = MyClass()
    print(a.x)
    print(a.y)
    a.x = 42
    print(a.x)

    d = Demo(2)
    print('Initial number:', d.i)
    print('Square number:', d.square)
    print('Writable square:')
    d.square = 42
    print('Read only:', d.normalize)
    print('Try write to d.normalize:')
    try:
        d.normalize = '[]'
    except TypeError as exc:
        print(exc)
