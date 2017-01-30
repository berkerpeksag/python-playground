"""
The __getitem__ version is a legacy before Python had
modern iterators.

Any sequence (something that is indexable and has a length)
would be automatically iterable using the series s[0], s[1], s[2],
...until IndexError or StopIteration is raised.
"""


class A:

    def __getitem__(self, index):
        if index >= 10:
            raise IndexError
        return index


class B:

    def __iter__(self):
        yield from range(10)


if __name__ == '__main__':
    a = A()

    print(list(a))

    for i in a:
        print(i)

    b = B()

    print(list(b))

    for i in b:
        print(i)
