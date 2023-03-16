from math import e
from math import factorial

# FIXME: Add a better description for the function docs for a better help() output


def subfactorial(n):
    """
    | Denoted by the !!n notation. Calculation of a number derangement.
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
