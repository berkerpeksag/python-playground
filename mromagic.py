"""
MRO Magic
---------

    >>> import mromagic
    >>> mycls = mromagic.C()
    >>> mycls
    <mromagic.C object at 0x622890>
    >>> mycls.c_method()
    C
    >>> mycls.a_method()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'C' object has no attribute 'a_method'
    >>> mycls.b_method()
    B
    >>> type(mycls).__mro__
    (<class 'mromagic.C'>, <class 'mromagic.B'>, <class 'object'>)
    >>> type(mycls).__bases__
    (<class 'mromagic.A'>,)

How does this work? By overriding ``mro()`` on the a metaclass we
can define a custom ``__mro__`` for our class. Python will then
traverse it instead of the default implementation, which is
provided by ``type.mro()``.

.. note::

   Note that although I'm using Python 3, this works with
   new-style class supporting versions.

http://pybites.blogspot.com/2009/01/mro-magic.html
"""


class A:

    def a_method(self):
        print('A')


class B:

    def b_method(self):
        print('B')


class MROMagicMeta(type):

    def mro(cls):
        return (cls, B, object)


class C(A, metaclass=MROMagicMeta):

    def c_method(self):
        print('C')
