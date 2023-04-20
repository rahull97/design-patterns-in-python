# A factory design pattern is used for wholesale creation of the object,
# as opposed to piecewise creation. It can be used when object creation
# logic becomes too convoluted or there are many optional params etc

from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def new_cartesian_point(x, y):  # factory method
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):  # factory method
        return Point(rho * cos(theta), rho * sin(theta))

    def __str__(self):
        return f"x: {self.x}, y:{self.y}"


if __name__ == "__main__":
    p1 = Point.new_cartesian_point(2, 3)
    p2 = Point.new_polar_point(1, 2)

    print(p1)
    print(p2)


# factory method: It is typically a method that creates an object of a class
