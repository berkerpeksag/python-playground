import functools


def partialize(func):
    def wrapper(*args, **kwargs):
        partial = functools.partial(func, *args, **kwargs)
        partial.__doc__ = func.__doc__
        return partial
    func.partial = wrapper
    return func


@partialize
def add(a, b):
    """Return result of a + b."""
    return a + b

if __name__ == '__main__':
    add_2 = add.partial(2)
    assert add.__doc__ == add_2.__doc__
    assert add_2(3) == 5
    assert add_2(-2) == 0
