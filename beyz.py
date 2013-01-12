"""
Simple usage:

    $ python beyz.py <base64_string> <data_type>
"""

import base64
import sys
import uuid

EXTENSIONS = ('png', 'jpg', 'gif',)


def usage():
    sys.stderr.write(__doc__)
    sys.exit()


def main():
    if len(sys.argv) != 3:
        usage()
    if sys.argv[2].lower() not in EXTENSIONS:
        usage()
    decoded_string = base64.b64decode(sys.argv[1])
    file_name = str(uuid.uuid1()) + '.' + sys.argv[2]
    with open(file_name, 'w') as fobj:
        fobj.write(decoded_string)
    print '{} created.'.format(file_name)

if __name__ == '__main__':
    main()