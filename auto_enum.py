import collections
import itertools


class AutoEnum(type):

    @classmethod
    def __prepare__(mcls, name, bases):
        return collections.defaultdict(itertools.count().__next__)

    def __new__(cls, name, bases, classdict):
        return type.__new__(cls, name, bases, dict(classdict))


class Enum(metaclass=AutoEnum):
    pass

if __name__ == '__main__':
    class MyEnum(Enum):
        apple
        orange

    print(MyEnum.apple, MyEnum.orange)
