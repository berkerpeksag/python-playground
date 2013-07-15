import dis
import types


def get_code_object(obj, compilation_mode="exec"):
    if isinstance(obj, types.CodeType):
        return obj
    if isinstance(obj, types.FrameType):
        return obj.f_code
    if isinstance(obj, types.FunctionType):
        return obj.__code__
    if isinstance(obj, str):
        try:
            return compile(obj, "<string>", compilation_mode)
        except SyntaxError as error:
            raise ValueError("syntax error in passed string") from error
    raise TypeError("get_code_object() can not handle '%s' objects" %
                        (type(obj).__name__,))


def diss(obj, mode="exec", recurse=False):
    _visit(obj, dis.dis, mode, recurse)


def ssc(obj, mode="exec", recurse=False):
    _visit(obj, dis.show_code, mode, recurse)


def _visit(obj, visitor, mode="exec", recurse=False):
    obj = get_code_object(obj, mode)
    visitor(obj)
    if recurse:
        for constant in obj.co_consts:
            if type(constant) is type(obj):
                print()
                print('recursing into %r:' % (constant,))
                _visit(constant, visitor, mode, recurse)
