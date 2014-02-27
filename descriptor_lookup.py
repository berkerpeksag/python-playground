from __future__ import print_function

class Foo(object):

    def my_function(self):
        return 42

if __name__ == '__main__':
    print(Foo.my_function)
    # <unbound method Foo.my_function>
    print(Foo.__dict__['my_function'])
    # <function my_function at 0x1002e1410>
    print(Foo.__dict__['my_function'].__get__(None, Foo))
    # <unbound method Foo.my_function>
    print(Foo().my_function)
    # <bound method Foo.my_function of <__main__.Foo object at 0x1002e2710>>
    print(Foo.__dict__['my_function'].__get__(Foo(), Foo))
    # <bound method Foo.my_function of <__main__.Foo object at 0x1002e2750>>
