# TODO: WHENEVER CREATING A SEQUENCE FUNCTION PLEASE TAKE TIME COMPLEXITY INTO CONSIDERATION, LOWEST POSSIBLE == BETTER
# TODO: RESOURCE FOR SEQUENCES, MAY VARY, BUT A 'GOTO' PAGE IS: https://oeis.org

from typing import Union


def atone(pos: Union[int, list, tuple]) -> Union[int, list, tuple]:
    """
    | Denoted by the expression (2ⁿ) - 1, n > 0
    | The 'Atone' sequence was named (unofficially) this way by Applied Mathematician Victor deMatos.
    | Atone sequence, derived from the latin 'atonen sequentia': meaning the sequence of ones.
    | Interestingly when you convert any of the numbers of this sequence to binary they are one-based numbers.
    | 1, 11, 111, 1111, 11111, 111111, -> the amount of ones is considered their degree in the sequence,
    | This sequence well-known as sir Johann Carl Friedrich Gauss binomial coefficient.
    | Victor deMatos qualifies it as Pascal's Triangle Displaced Degrees.
    | (see https://gist.github.com/shimon-d/20ec381f8865eb55311328dbb56d5462)
    | Returns the sequence's number in a given position, or positions.
    | Accepting either integers or lists.
    | atone(10) -> 1023
    | If the value entered is not acceptable the function returns -1
    """

    if type(pos) == int:
        pos = abs(pos)
        pos = pow(2, pos) - 1
        return pos
    if type(pos) in [list, tuple]:
        try:
            pos = list(map(lambda n: abs(n), pos))
            pos = list(map(lambda n: int(n * '1', 2), pos))
            return pos
        except TypeError:
            return -1
    else:
        return -1
