from __future__ import print_function


def func(x=42):
    y = x * 3
    return y


if __name__ == '__main__':
    code_obj = func.func_code
    print('co_name', code_obj.co_name)
    print('co_filename', code_obj.co_filename)
    print('co_argcount', code_obj.co_argcount)
    print('co_varnames', code_obj.co_varnames)
    print('co_consts', code_obj.co_consts)
    print('co_code', repr(code_obj.co_code))
