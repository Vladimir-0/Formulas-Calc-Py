from decimal import Decimal, DivisionByZero
from typing import Union

_func = [
    lambda x, y: 5 * x + 10 / y,
    lambda x, y: 3 * x ** 2 + y + 3,
    lambda x, y: (x + 10 * y) / 3
]


def perform_operation(x: Decimal, y: Decimal, formula_num: int) -> Union[Decimal, str]:
    """
    Performs operation on 2 numbers.
    :param x: First argument.
    :param y: Second argument.
    :param formula_num: Operation number.
    :return: The calculation result.
    """
    try:
        result = _func[formula_num](x, y)
    except KeyError:
        return "Incorrect operation"
    except DivisionByZero:
        return "Impossible to divide by 0"
    return result
