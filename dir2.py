from __future__ import print_function

import fnmatch
import sys

_sentinel = object()


def dir2(obj=_sentinel, glob=None):
    """
    Usage::

        >>> list(dir2(decimal.Decimal, '*log*'))
        ['_fill_logical', '_islogical', '_log10_exp_bound', 'log10', 'logb',
        'logical_and', 'logical_invert', 'logical_or', 'logical_xor']

    """
    if obj is _sentinel:
        # Get the locals of the caller, not our locals.
        names = sorted(sys._getframe(1).f_locals)
    else:
        names = dir(obj)
    if glob is None:
        return names
    return (name for name in names if fnmatch.fnmatchcase(name, glob))

if __name__ == '__main__':
    import decimal
    print(list(dir2(decimal.Decimal, '*log*')))
    print()
    print(list(dir2(object, '*__*')))
