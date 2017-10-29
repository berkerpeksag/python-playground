def compose(*funcs):
    """
    Return a new function from *funcs.
    compose(f, g)(x) is an equivalent of f(g(x)).
    """
    def inner(data, funcs=funcs):
        result = data
        for func in reversed(funcs):
            result = func(result)
        return result
    return inner


def b(s):
    return '<b>{}</b>'.format(s)


def i(s):
    return '<i>{}</i>'.format(s)

if __name__ == '__main__':
    composed = compose(b, i)
    print(composed('berker'))
    print('Usual way:')
    print(b(i('berker')))
