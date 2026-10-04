"""!
@file test_operations.py
@brief Tests for the arithmetic operations.
"""

import pytest

from calc.operations import OPERATIONS, add, divide, multiply, subtract


def test_add_returns_sum() -> None:
    assert add(2, 3) == 5


def test_subtract_returns_difference() -> None:
    assert subtract(2, 3) == -1


def test_multiply_returns_product() -> None:
    assert multiply(4, 2.5) == 10


def test_divide_returns_quotient() -> None:
    assert divide(9, 3) == 3


def test_divide_when_divisor_is_zero() -> None:
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_operations_maps_symbols_to_functions() -> None:
    assert OPERATIONS == {"+": add, "-": subtract, "*": multiply, "/": divide}
