"""
Usage::

    $ python settrace.py <FILE>
"""

import sys


def trace(frame, event, arg):
    filename = frame.f_code.co_filename
    lineno = frame.f_lineno
    print '{:s} @ {:d}: {:s}'.format(filename, lineno, event)
    return trace


def run_py(py_file):
    sys.settrace(trace)
    exec open(py_file) in {}
    sys.settrace(None)

if __name__ == '__main__':
    run_py(sys.argv[1])
