# When using this lib import give preference to the full file/package import:
# from functvs import common, in the stead of from functvs import sin
# to avoid having any overlaps with -> math imports


def sine(x):
    """
    | :param x: The angle in radians
    | :return: The sine of x
    | Compute the sine of x using a Taylor series approximation.
    | CORDIC (Coordinate Rotation Digital Computer) is an algorithm developed by Jack E. Volder in 1959
    | while he was working at Convair (later General Dynamics), an aerospace and defense company.
    | source: https://math.stackexchange.com/questions/4378919/algorithm-behind-sin-function
    """

    if not isinstance(x, (int, float)):
        raise ValueError("Input must be a number")

    epsilon = 0.1e-16  # Error tolerance
    sinus = 0.0  # Sine of x
    sign = 1  # Sign of the current term
    current_term = x  # Current term in the series
    n = 1  # Current term number

    # Calculate sine using the Taylor series approximation
    while abs(current_term) > epsilon:
        sinus += sign * current_term
        sign = -sign
        current_term *= x * x / (n + 1) / (n + 2)
        n += 2

    return sinus
