def memoize(func):
    cache = {}

    def inner(*args):
        if args in cache:
            print('HIT:', args)
            return cache[args]
        res = func(*args)
        cache[args] = res
        return res
    return inner


if __name__ == '__main__':
    @memoize
    def add(x, y):
        return x + y

    add(2, 2)
    add(2, 2)
    add(2, 2)
