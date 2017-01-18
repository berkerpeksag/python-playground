class Train:
    """
    This class implements the classic iterator pattern
    that explained in the famous Gang of Four book.
    """

    def __init__(self, number):
        self.number = number
        self.next = 0

    def __iter__(self):
        return self

    def __next__(self):
        # We could move this method into a separate
        # TrainIterator class.
        if self.next < self.number:
            self.next += 1
            return 'car #{:d}'.format(self.next)
        raise StopIteration


class TrainSimplified:
    """
    The above pattern is obsolote in Python since
    2.2 released in 2001.
    """

    def __init__(self, number):
        self.number = number

    def __iter__(self):
        # This is now iterable because __iter__
        # returns a generator.
        # We could also use a generator expression
        # here to make things simpler.
        for i in range(1, self.number+1):
            yield 'car #{:d}'.format(i)


if __name__ == '__main__':
    t = Train(3)
    for car in t:
        print(car)

    t2 = TrainSimplified(5)
    for car in t2:
        print(car)
