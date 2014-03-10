class MyInt(int):
    def __add__(self, other):
        print 'Specializing addition.'
        return super(MyInt, self).__add__(other)


class Test(object):
    def __init__(self, number):
        self.number = number

    def __int__(self):
        return self.number

    def __add__(self, add):
        return int(self.__class__(int(self) + int(add)))

if __name__ == '__main__':
    i = MyInt(4)
    print i + 2
    t = Test(1)
    t2 = Test(2)
    print t + t2
    print t + 31
