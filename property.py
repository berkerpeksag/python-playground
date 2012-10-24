class Property(object):
    """Emulate PyProperty_Type() in Objects/descrobject.c

    Signature of property():

    property(fget=None, fset=None, fdel=None, doc=None)
    """

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)


def main():
    c = C()
    print c.x
    c.x = 'Spam'
    print c.x

if __name__ == '__main__':
    main()
