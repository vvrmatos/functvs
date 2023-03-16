from math import sqrt
from math import pow
from typing import Union


class Pythagoras:
    """The sum of the legs squared is the Hypotenuse squared"""

    @staticmethod
    def leg_hypotenuse(
        a: Union[int, float] = None,
        b: Union[int, float] = None,
        c: Union[int, float] = None,
    ):
        if a and b and not c:
            a = pow(a, 2)
            b = pow(b, 2)
            return sqrt(a + b)

        if a and c and not b:
            a = pow(a, 2)
            c = pow(c, 2)
            return sqrt(abs(a - c))

        if b and c and not a:
            b = pow(b, 2)
            c = pow(c, 2)
            return sqrt(abs(b - c))

        if a and b and c:
            a = pow(a, 2)
            b = pow(b, 2)
            return sqrt(a + b)

    @staticmethod
    def perimeter(
        a: Union[int, float] = None,
        b: Union[int, float] = None,
        c: Union[int, float] = None,
    ):
        return a + b + c


class Euclid:
    """An isosceles triangle is defined as a triangle with at least two equal sides
    from Greek Isoskeles "with equal legs" """

    @staticmethod
    def isosceles_area(base, height):
        return (base * height) / 2
