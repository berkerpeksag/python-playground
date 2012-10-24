class C(object):
    def __init__(self):
        self.__x = 'Eggs'

    def getx(self):
        return self.__x

    def setx(self, value):
        self.__x = value

    def delx(self):
        del self.__x

    # or use decorator style
    x = property(getx, setx, delx, "I'm the 'x' property.")


def main():
    c = C()
    print c.x
    c.x = 'Spam'
    print c.x

if __name__ == '__main__':
    main()
