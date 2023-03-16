import math
from math import e
from math import factorial


class Subfactorial:
    @staticmethod
    def recursive(n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 0
        else:
            return (n - 1) * (
                Subfactorial.recursive(n - 1) + Subfactorial.recursive(n - 2)
            )

    @staticmethod
    def euler(n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 0
        return int((factorial(n) + 1) / e)


class Factorial:
    @staticmethod
    def factorial(n):
        return math.factorial(n)
