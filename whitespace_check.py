from __future__ import print_function, unicode_literals

import string


def check_whitespace(strn):
    return any(s in string.whitespace for s in strn)

if __name__ == '__main__':
    tests = (
        'berker', 'berker peksag', '  berker', 'berker ',
        '\tber\n',
    )
    for test in tests:
        print(test, check_whitespace(test))
