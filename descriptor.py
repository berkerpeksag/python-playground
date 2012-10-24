class RevealAccess(object):
    """A data descriptor that sets and returns values
    normally and prints a message logging their access."""

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print 'Retrieving', self.name
        print obj, objtype
        return self.val

    def __set__(self, obj, val):
        print 'Updating' , self.name
        self.val = val


class MyClass(object):
    x = RevealAccess(10, 'x')
    y = 5


def main():
    a = MyClass()
    print a.x
    print a.y
    a.x = 42
    print a.x

if __name__ == '__main__':
    main()
