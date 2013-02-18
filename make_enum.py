# Thread from here:
# http://mail.python.org/pipermail/python-ideas/2013-February/019410.html
import types


def make_enum(keys, *, value=None):
    """For incremental numbers: ``lambda key, index: index``.
    For bitwise flags: ``lambda key, index: 2**index``.

    Could change to take an iterator instead of a lambda and
    simply special-case the `None` argument for strings, but
    that seems needlessly limiting when the integer case is
    probably for interfacing with some C code.
    """
    if value is None:
        value = lambda key, index: key
    items = {}
    for key, index in enumerate(keys.split()):
        items[key] = value(key, index)
    # Creating a read-only subclass is trivial
    return types.SimpleNamespace(**items)
