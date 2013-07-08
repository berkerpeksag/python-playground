"""
Some monkeypatching recipes.

See for the discussion about using monkeypatching in Python:
http://mail.python.org/pipermail/python-dev/2008-January/076194.html
"""


def monkeypatch_method(cls):
    """
    A decorator to add a single method to an existing class.

    To use::

        from <somewhere> import <someclass>

        @monkeypatch_method(<someclass>)
        def <newmethod>(self, args):
            return <whatever>

    This adds <newmethod> to <someclass>.
    """

    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator


def monkeypatch_class(name, bases, namespace):
    """
    A "metaclass" to add a number of methods (or other attributes)
    to an existing class, using a convenient class notation.

    To use::

        from <somewhere> import <someclass>

        class <newclass>(<someclass>,  metaclass=monkeypatch_class):

            def <method1>(...):
                # ...

            def <method2>(...):
                # ...

    This adds <method1>, <method2>, etc. to <someclass>, and makes
    <newclass> a local alias for <someclass>.
    """

    assert len(bases) == 1, "Exactly one base class required"
    base = bases[0]
    for name, value in namespace.items():
        if name != "__metaclass__":
            setattr(base, name, value)
    return base
