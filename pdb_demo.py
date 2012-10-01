"""
Usage
-----

From the command line::

    $ python -m pdb pdb_script.py

Within the interpreter::

    >>> import pdb_demo
    >>> import pdb
    >>> pdb.run('pdb_demo.MyObj(5).go()')
    > <string>(1)<module>()
    (Pdb)

From within your program::

    import pdb

    # ...
    pdb.set_trace()

http://www.doughellmann.com/PyMOTW/pdb/
"""

class MyObj(object):

    def __init__(self, num_loops):
        self.count = num_loops

    def go(self):
        for i in range(self.count):
            # pdb.set_trace()
            print i
        return

if __name__ == '__main__':
    MyObj(5).go()
