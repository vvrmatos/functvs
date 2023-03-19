from math import factorial


def b_catalan(row):
    """
    | Type B Catalan numbers also known as Binomial Coefficient.
    """
    return factorial(2 * row) // factorial(row) ** 2


def triangular_numbers(n):
    """
    | Triangular Numbers Sequence, the third row in Pascal's triangle.
    | 1 1 1 1 ->  Row n1
    | 1 2 3 4 ->  Row n2
    | 1 3 6 10 -> Row n3
    | Which represents a summation of the row above,
    | from the first element up to the current wished column index.
    | Where n > 0.
    """
    n = abs(n) + 1
    n = (n * (n + 1)) // 2
    return n


def triangular_pyramid(n):
    n = abs(n) + 1
    n = (n * (n + 1) * (n + 2)) // 6
    return n


def second_kind_triangular_number(n: int):
    """
    | :param n: Positive column index on the fourth row of Pascal triangle
    | Triangular numbers of the second kind
    | Pascal's triangle 5th row.
    """
    n = abs(n) + 4
    n = n * (n - 1) * (n - 2) * (n - 3) // 24
    return n


def pascal(row, column):
    pass
