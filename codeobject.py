# coding: utf-8

def func(x=42):
    y = x * 3
    return y


def main():
    code_obj = func.func_code
    print code_obj.co_name
    print code_obj.co_filename
    print code_obj.co_argcount
    print code_obj.co_varnames
    print code_obj.co_consts
    print code_obj.co_code

if __name__ == '__main__':
    main()
