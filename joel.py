# coding: utf-8

"""
Some easy questions to ask an interviewer from Joel Spolsky:

1) Write a function that determines if a string starts with an upper-case
   letter A-Z
2) Write a function that determines the area of a circle given the radius
3) Add up all the values in an array
"""

import re


def starts_with_uppercase(s):
    # XXX: s[0] ile daha mı hızlı olur?
    # XXX: regex haricinde daha hızlı bir yöntem var mı?
    if not isinstance(s, (basestring, buffer)):
        return False
    return bool(re.match(r'^[A-Z]', s))

if __name__ == '__main__':
    test_strings = (1212, 'berker', 'Peksag', '_foo', '12berker',)
    for _str in test_strings:
        print _str, starts_with_uppercase(_str)
