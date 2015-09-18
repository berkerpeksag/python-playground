"""
A decorator factory is a function that returns a decorator.

Decorator factories are used when you want to pass additional
argument to the decorator, and they are commonly implemented
by nesting 3 functions.

The outer function is the decorator factory, the middle one
is the decorator, and the inner one is the function that will
replace the decorated function.

"""

import functools


def repeat_for(times):
    def deco(func):
        @functools.wraps(func)
        def inner():
            for x in range(times):
                func()
        return inner
    return deco


@repeat_for(3)
def hello():
    print("hello")


@repeat_for(2)
def bye():
    print("bye")

# same as bye = repeat_for(2)(bye)

hello()
bye()


def tags(tag_name):
    def tags_decorator(func):
        @functools.wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator


@tags("p")
def get_text(name):
    """Return some text."""
    return "Hello {}".format(name)


def get_text_not_decorated(name):
    """Return some text."""
    return "Hello {}".format(name)


print(get_text("Lindsay"))
print(tags("p")(get_text_not_decorated)("Lindsay"))
