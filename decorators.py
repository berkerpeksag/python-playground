# http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/

from __future__ import print_function


a_str = 'foooo'


def foo():
    local_var = 'lindsay'
    return locals()


print(globals())

print(foo())


def bar(x=None):
    return locals()


print(bar())
print(bar(42))


def outer():
    x = 1
    def inner():
        return x
    return inner()


print(outer())


def outer2():
    x = 1
    def inner():
        return x
    return inner


print(outer2()())
print(outer2().func_closure)

def baz():
    pass


print(baz.__class__)


def outer3(x):
    def inner():
        return x
    return inner


return2 = outer3(2)
print(return2)
print(return2())
return42 = outer3(42)
print(return42())
print(outer3(31)())


def outer4(some_func):
    def inner():
        print('Before "%s"' % some_func.__name__)
        ret = some_func()
        return ret + 1
    return inner


def foo2():
    return 1


decorated = outer4(foo2)
print(decorated())


def wrapper(func):
    def checker(a, b):
        print('Function name "%s"' % func.__name__)
        print('a', a)
        print('b', b)
        return '[[%s]]' % ','.join(map(str, func(a, b)))
    return checker


def test(a, b):
    return a, b


test = wrapper(test)
print(test(24, 42))


def logger(func):
    def inner(*args, **kwargs):
        print('Arguments for "%s" were: %s, %s' % (func.__name__, args, kwargs))
        return func(*args, **kwargs)
    return inner


@logger
def foo3(*args):
    return args


print(foo3(*range(5)))
