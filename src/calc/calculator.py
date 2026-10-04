"""!
@file calculator.py
@brief The interactive console calculator.
"""

from calc.constants import (
    ANSWER_CONTINUE,
    ANSWER_NEW,
    ANSWER_QUIT,
    ASCII_TITLE,
    MESSAGE_DIVIDE_BY_ZERO,
    MESSAGE_GOODBYE,
    MESSAGE_INVALID_ANSWER,
    MESSAGE_INVALID_NUMBER,
    MESSAGE_INVALID_OPERATION,
    PROMPT_AGAIN,
    PROMPT_FIRST_NUMBER,
    PROMPT_NEXT_NUMBER,
    PROMPT_OPERATION,
)
from calc.operations import OPERATIONS


def format_number(value: float) -> str:
    """!
    @brief Format a number without a trailing ".0" for whole values.
    @param value The number to format.
    @return The text to show the user.
    """
    return str(int(value)) if value.is_integer() else str(value)


def read_number(prompt: str) -> float:
    """!
    @brief Ask for a number until the user types a valid one.
    @param prompt The text shown to the user.
    @return The number typed by the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(MESSAGE_INVALID_NUMBER)


def read_operation() -> str:
    """!
    @brief Show the available operations and ask for one until it is valid.
    @return The symbol of the chosen operation, a key of OPERATIONS.
    """
    for symbol in OPERATIONS:
        print(symbol)
    while True:
        symbol = input(PROMPT_OPERATION).strip()
        if symbol in OPERATIONS:
            return symbol
        print(MESSAGE_INVALID_OPERATION)


def read_answer(result: float) -> str:
    """!
    @brief Ask whether to continue with the result, start anew or quit.
    @param result The result of the last calculation.
    @return One of ANSWER_CONTINUE, ANSWER_NEW or ANSWER_QUIT.
    """
    while True:
        answer = input(PROMPT_AGAIN.format(result=format_number(result)))
        answer = answer.strip().lower()
        if answer in (ANSWER_CONTINUE, ANSWER_NEW, ANSWER_QUIT):
            return answer
        print(MESSAGE_INVALID_ANSWER)


def calculator() -> None:
    """!
    @brief Run one calculation session.

    The user may continue with the previous result. Starting a new
    calculation calls this function again (recursion), which gives a clean
    restart. A division by zero also restarts the calculator.
    """
    num1 = read_number(PROMPT_FIRST_NUMBER)
    while True:
        symbol = read_operation()
        num2 = read_number(PROMPT_NEXT_NUMBER)
        try:
            result = OPERATIONS[symbol](num1, num2)
        except ZeroDivisionError:
            print(MESSAGE_DIVIDE_BY_ZERO)
            calculator()
            return
        print(
            f"{format_number(num1)} {symbol} {format_number(num2)} "
            f"= {format_number(result)}"
        )
        answer = read_answer(result)
        if answer == ANSWER_CONTINUE:
            num1 = result
        elif answer == ANSWER_NEW:
            calculator()
            return
        else:
            print(MESSAGE_GOODBYE)
            return


def main() -> None:
    """!
    @brief Program entry point: show the ASCII title and start the calculator.
    """
    print(ASCII_TITLE)
    calculator()
