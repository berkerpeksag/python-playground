"""
Usage
-----

    $ python beyz.py data:image/png;base64,iVBORw0KGgoAAAANSUhEUgA

"""

import base64
import sys
import uuid

EXTENSIONS = ('png', 'jpg', 'gif',)


def usage():
    sys.stderr.write(__doc__)
    sys.exit()


def main():
    if len(sys.argv) != 2:
        usage()
    b64_type, b64_str = sys.argv[1].split(';base64,')
    if not b64_type.endswith(EXTENSIONS):
        usage()
    decoded_string = base64.b64decode(b64_str)
    file_name = str(uuid.uuid1()) + '.' + b64_type[-3:]
    with open(file_name, 'w') as fobj:
        fobj.write(decoded_string)
    print '{} created.'.format(file_name)

if __name__ == '__main__':
    main()
