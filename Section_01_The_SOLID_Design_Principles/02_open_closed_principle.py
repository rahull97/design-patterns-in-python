# OCP stands for open for extension, closed for modification.
# In other words it means that new functionality must be added
# by extending or creating new classes rather than modifying
# existing classes.
# Code should be always open for extension but closed for modification.


from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


# Implementing product filter feature by following open close principle
class Specification:
    """Base class for specifying filtering spec"""
    def is_satisfied(self, item):
        pass


class Filter:
    """Base filter class"""
    def filter(self, items, spec):
        pass


# create specific implementations. New implementations can be added by
# adding new classes and existing code does not need to be modified
class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == "__main__":
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)

    products = [
        apple,
        tree,
        house
    ]

    green = ColorSpecification(Color.GREEN)
    large = SizeSpecification(Size.LARGE)
    large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))

    bf = BetterFilter()

    for p in bf.filter(products, green):
        print(f' - {p.name} is green\n')

    for p in bf.filter(products, large):
        print(f' - {p.name} is large\n')

    for p in bf.filter(products, large_blue):
        print(f' - {p.name} is large and blue\n')
