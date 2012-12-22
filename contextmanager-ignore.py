# coding: utf-8

"""
Add context manager for the ``try: ... except: pass`` pattern.

It is a somewhat common pattern to write::

    try:
        do_something()
    except SomeException:
        pass

See for more information: http://bugs.python.org/issue15806
"""

from contextlib import contextmanager


@contextmanager
def ignored(*exceptions):
    """Context manager to ignore particular exceptions.

    While the class based version would likely be fractionally
    faster, the generator based version is more obviously
    correct.
    """
    try:
        yield
    except exceptions:
        pass


class Ignore:
    """Context manager to ignore particular exceptions."""

    def __init__(self, *ignored_exceptions):
        self.ignored_exceptions = ignored_exceptions

    def __enter__(self):
        return self

    def __exit__(self, exctype, excinst, exctb):
        return exctype and issubclass(exctype, self.ignored_exceptions)


def main():
    dct = {}

    # decorator version
    with ignored(KeyError):
        del dct['spam']

    # class-based version
    with Ignore(KeyError):
        del dct['spam']

    try:
        del dct['spam']
    except KeyError:
        pass

if __name__ == '__main__':
    main()
