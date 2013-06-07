FOO = 'BAR'


class A(object):
    pass


class B(object):
    pass

if __name__ == '__main__':
    import inspect
    import sys

    classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for cls in classes:
        print(cls)
