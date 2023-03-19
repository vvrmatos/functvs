from math import e
from math import factorial
from math import pow
from fractions import Fraction


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


def gamma(n):
    """
    | Denoted by the Γ symbol, the Gamma function is a piece of work done in collaboration
    | over the years by many mathematicians, Leonhard Euler most notably in 1730.
    | Euler expanded the studies on the function that is a sophisticated integration by parts.
    | That can be represented as: ∫ₐᵇ u' . v = u . v | ₐᵇ - ∫ₐᵇ u . v'
    | The proposed integral being: ∫₀∞ xⁿ⁻¹ . e⁻ˣ . dx
    """
    n = __import__("math").gamma(n)
    return n


def beta(m, n):
    res = (gamma(m) * gamma(n)) / gamma(m + n)
    return Fraction(res).limit_denominator(1_000_000_000_000_000)


def alpha(n):
    """
    | The alpha function, denoted by α(n), is a special function in mathematics that is closely related to the gamma
    | function and the beta function. It is defined as:
    | α(n) = [(π/2)^(n/2)] * R^n / Γ(n/2 + 1)
    | where R is a constant and Γ(x) is the gamma function.
    | The values presented here, are not as accurate for numbers under 5-6

    """

    # Rough approximation
    res = (
        1
        - (1 / (12 * n))
        + (1 / (288 * pow(n, 2)))
        - (139 / (51840 * pow(n, 3)))
        + (571 / (2488320 * pow(n, 4)))
        - (163879 / (209018880 * pow(n, 5)))
        + (5246819 / (75246796800 * pow(n, 6)))
    )

    return res
