from math import factorial


def b_catalan(row):
    """
    | Type B Catalan numbers also known as Binomial Coefficient.
    """
    return factorial(2 * row) // factorial(row) ** 2
