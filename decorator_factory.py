"""
A decorator factory is a function that returns a decorator.

Decorator factories are used when you want to pass additional
argument to the decorator, and they are commonly implemented
by nesting 3 functions.

The outer function is the decorator factory, the middle one
is the decorator, and the inner one is the function that will
replace the decorated function.

"""


def repeat_for(times):
    def deco(func):
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
