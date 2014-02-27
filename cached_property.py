"""
Usage::

    class Spam(object):

        def __init__(self, text):
            self.text = text

        @cached_property
        def rendered(self):
            return markdown(self.text)

"""

missing = object()


class CachedProperty(object):

    def __init__(self, func):
        self.func = func
        self.__name__ = func.__name__
        self.__doc__ = func.__doc__
        self.__module__ = func.__module__

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        value = obj.__dict__.get(self.__name__, missing)
        if value is missing:
            value = self.func(obj)
            obj.__dict__[self.__name__] = value
        return value


cached_property = CachedProperty
