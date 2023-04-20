# A factory class allows us to group factory methods and operate as
# a separate entity. This helps us to follow to SOLID design principles
# in a better way

from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x}, y:{self.y}"

    class PointFactory:  # factory class can be inner class or a specific separate class
        @staticmethod
        def new_cartesian_point(x, y):  # factory method, can be static or non-static, depends on situation.
            return Point(x, y)

        @staticmethod
        def new_polar_point(rho, theta):  # factory method
            return Point(rho * cos(theta), rho * sin(theta))

    factory = PointFactory()  # acts as a singleton object.


if __name__ == "__main__":
    p1 = Point.factory.new_cartesian_point(2, 3)
    p2 = Point.factory.new_polar_point(1, 2)

    print(p1)
    print(p2)
