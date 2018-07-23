@object.__new__
class spam:

    def __new__(cls):
        raise TypeError(
            'cannot create {!r} instances'.format(type(cls).__name__)
        )

    @staticmethod
    def __getitem__(key):
        return key

if __name__ == '__main__':
    print(spam, type(spam))
    print(spam[0])
    print(spam[None])
    print(spam[spam])
    spam()  # TypeError: 'spam' object is not callable
    spam.__new__(spam)  # TypeError: cannot create 'spam' instances
