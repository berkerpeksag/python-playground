class A(object):

    def __getattr__(self, name):
        print name
        return name

    def __setattr__(self, name, value):
        self.__dict__[name] = value
        A.__setattr__(self, name, value)


def main():
    a = A()
    print a.a, a.b

if __name__ == '__main__':
    main()
