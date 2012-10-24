import types


class Function(object):
    # ...
    def __get__(self, obj, objtype=None):
        """Simulate func_descr_get() in Objects/funcobject.c"""
        return types.MethodType(self, obj, objtype)
