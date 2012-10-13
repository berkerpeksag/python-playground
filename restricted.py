# coding: utf-8

"""
Execution of restricted Python code.

Use with `evil.py`::

    $ python restricted.py evil.py

https://gist.github.com/3437909
"""

import platform
import pprint
import os
import sys


def _restrict(filename, debug=False):
    # always add a newline, compile needs one in Python < 2.7.
    source = open(filename, 'r').read() + '\n'

    code = compile(source, filename, 'exec')
    global_ns = {
        '__builtins__': {
            'False': False,
            'None': None,
            'True': True,
        },
        'uname': platform.uname(),
    }
    local_ns = {}
    exec code in global_ns, local_ns

    if debug:
        print 'Globals'
        pprint.pprint(global_ns)
        print 'Locals'
        pprint.pprint(local_ns)


def main(filename):
    filename = os.path.abspath(os.path.normpath(os.path.expandvars(
        os.path.expanduser(filename))))
    if not os.path.isfile(filename):
        raise IOError('File not found: {0:s}'.format(filename))

    _restrict(filename, debug=True)


if __name__ == '__main__':
    main(sys.argv[1])
