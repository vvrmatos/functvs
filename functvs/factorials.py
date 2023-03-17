from math import e
from math import factorial
from typing import Union


# FIXME: Add a better description for the function docs for a better help() output
# TODO: Some functions return -1 as an error yet, implement a better fashioned way of doing it


def subfactorial(n):
    """
    | Denoted by the !n notation. Calculation of a number derangement.
    """
    if n == 0:
        return 1
    if n == 1:
        return 0
    return int((factorial(n) + 1) / e)


def double_factorial(n):
    """
    | Denoted by the n!! notation
    """
    if n < 0:
        return None
    result = 1
    for i in range(n, 0, -2):
        result *= i
    return result


def b_coefficients(row):
    """
    | The numbers in the centre of Pascal's Triangle. Return number in the row.
    """
    return factorial(2 * row) // factorial(row) ** 2


def gamma(n: int) -> int:
    """
    | Denoted by the Γ symbol, the Gamma function is a piece of work done in collaboration
    | over the years by many mathematicians, Leonhard Euler most notably in 1730.
    | Euler expanded the studies on the function that is a sophisticated integration by parts.
    | That can be represented as: ∫ₐᵇ u' . v = u . v | ₐᵇ - ∫ₐᵇ u . v'
    | The proposed integral being: ∫₀∞ xⁿ⁻¹ . e⁻ˣ . dx
    """
    if n > 0:
        return factorial(n - 1)
    return -1


def beta():
    pass


def alpha():
    pass


def least_squares(n: Union[float, int]):
    """
    | Denoted by n!, where 0 <= n <= 1, n! == Γ(n + 1)
    """

    if 0 <= n <= 1:
        # The Least Square rule for 0 and 1
        if 0 == n == 1:
            return 1

        # Least Square Factorial Function
        exp = (
            1
            - (0.574 * pow(n, 1))
            + (0.951 * pow(n, 2))
            - (0.699 * pow(n, 3))
            + (0.424 * pow(n, 4))
            - (0.101 * pow(n, 5))
        )

        return exp
    return -1
