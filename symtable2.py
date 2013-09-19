"""
Pythonic API of the symtable module

See the documentation: http://docs.python.org/3.4/library/symtable.html

"""

import symtable


class SymbolTable(object):

    @property
    def type(self):
        raise NotImplementedError

    @property
    def id(self):
        raise NotImplementedError


class Class(SymbolTable):

    @property
    def methods(self):
        raise NotImplementedError
