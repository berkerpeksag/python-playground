from __future__ import print_function, unicode_literals

import string


def check_whitespace(strn):
    return any(map(lambda s: s in string.whitespace, strn))

if __name__ == '__main__':
    tests = ('berker', 'berker peksag', '  berker', 'berker ',
             '\tber\n',)
    for test in tests:
        print(test, check_whitespace(test))
