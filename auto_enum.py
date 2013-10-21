import collections
import itertools


class AutoEnum(type):

    @classmethod
    def __prepare__(metacls, name, bases):
        return collections.defaultdict(itertools.count().__next__)

    def __new__(cls, name, bases, classdict):
        result = type.__new__(cls, name, bases, dict(classdict))
        return result


class Enum(metaclass=AutoEnum):
    pass

if __name__ == '__main__':
    class MyClass(Enum):
        apple
        orange

    print(MyClass.apple, MyClass.orange)
