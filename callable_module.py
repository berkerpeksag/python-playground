"""
A module can define a class with the desired functionality, and then
at the end, replace itself in sys.modules with an instance of that
class (or with the class, if you insist, but that's generally less
useful).

    import callable_module
    print(callable_module.bar('lindsay'))

"""

import sys

class Foo:

    def bar(self, name):
        return name

sys.modules[__name__] = Foo()
