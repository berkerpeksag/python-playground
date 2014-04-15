def husrange(i):
    c = 0
    while c < i:
        yield c
        c += 1

if __name__ == '__main__':
    print [i for i in husrange(10)]
