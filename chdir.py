"""
My response to "chdir context manager" discussion on python-ideas.


Usage
-----

.. code-block:: python
    with chdir('foo/bar'):
        # do something useful

    with chdir():  # creates a directory in /tmp
        # do something useful


Cons
----

* Anti-pattern. Paths should be converted to absolute ASAP, and for invocation
  of other tools that care about the current directory, that's why the
  subprocess APIs accept a "cwd" argument.
* It's not thread safe. You can NOT make it work properly and safe in a
  multi-threaded environment or from code like signal handlers.
* It's a major race condition.


Solution
--------

The Open Group has acknowledged the issue and added a new set of
functions to POSIX.1-2008 in order to address the issue. The *at()
variants of functions like open() take an additional file descriptor as
first argument. The fd must refer to a directory and is used as base for
relative paths. Python 3.3 supports the new *at() feature.


References
==========

* http://mail.python.org/pipermail/python-ideas/2013-January/018756.html
* http://en.wikipedia.org/wiki/Open_%28system_call%29#C_library_POSIX_definition
"""

import contextlib
import os
import shutil
import tempfile


@contextlib.contextmanager
def chdir(d=None):
    is_temporary = False
    cwd = os.getcwd()
    if d is None:
        d = tempfile.mkdtemp()
        is_temporary = True
    try:
        yield os.chdir(d)
    finally:
        if is_temporary:
            shutil.rmtree(d)
        os.chdir(cwd)
