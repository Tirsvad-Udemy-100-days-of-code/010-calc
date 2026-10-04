"""!
@file operations.py
@brief Arithmetic operations and the dictionary that maps symbols to them.
"""

from collections.abc import Callable

from calc.constants import (
    SYMBOL_ADD,
    SYMBOL_DIVIDE,
    SYMBOL_MULTIPLY,
    SYMBOL_SUBTRACT,
)


def add(n1: float, n2: float) -> float:
    """!
    @brief Add two numbers.
    @param n1 The first number.
    @param n2 The second number.
    @return The sum of @p n1 and @p n2.
    """
    return n1 + n2


def subtract(n1: float, n2: float) -> float:
    """!
    @brief Subtract the second number from the first.
    @param n1 The first number.
    @param n2 The second number.
    @return The difference @p n1 minus @p n2.
    """
    return n1 - n2


def multiply(n1: float, n2: float) -> float:
    """!
    @brief Multiply two numbers.
    @param n1 The first number.
    @param n2 The second number.
    @return The product of @p n1 and @p n2.
    """
    return n1 * n2


def divide(n1: float, n2: float) -> float:
    """!
    @brief Divide the first number by the second.
    @param n1 The dividend.
    @param n2 The divisor.
    @return The quotient @p n1 divided by @p n2.
    @throws ZeroDivisionError When @p n2 is zero.
    """
    return n1 / n2


## Maps an operation symbol to its function. The functions are stored, not called.
OPERATIONS: dict[str, Callable[[float, float], float]] = {
    SYMBOL_ADD: add,
    SYMBOL_SUBTRACT: subtract,
    SYMBOL_MULTIPLY: multiply,
    SYMBOL_DIVIDE: divide,
}
