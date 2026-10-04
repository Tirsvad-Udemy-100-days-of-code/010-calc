"""!
@file constants.py
@brief Constants used by the console calculator.
"""

## Operation symbols, in the order they are offered to the user.
SYMBOL_ADD: str = "+"
SYMBOL_SUBTRACT: str = "-"
SYMBOL_MULTIPLY: str = "*"
SYMBOL_DIVIDE: str = "/"

## Answers accepted after a calculation.
ANSWER_CONTINUE: str = "y"
ANSWER_NEW: str = "n"
ANSWER_QUIT: str = "q"

## Prompts and messages shown to the user.
PROMPT_FIRST_NUMBER: str = "What's the first number?: "
PROMPT_NEXT_NUMBER: str = "What's the next number?: "
PROMPT_OPERATION: str = "Pick an operation: "
PROMPT_AGAIN: str = (
    f"Type '{ANSWER_CONTINUE}' to continue calculating with {{result}}, "
    f"'{ANSWER_NEW}' to start a new calculation, "
    f"or '{ANSWER_QUIT}' to quit: "
)
MESSAGE_INVALID_NUMBER: str = "That is not a number, please try again."
MESSAGE_INVALID_OPERATION: str = "That is not a valid operation, please try again."
MESSAGE_INVALID_ANSWER: str = "Please answer with one of the listed letters."
MESSAGE_DIVIDE_BY_ZERO: str = "You cannot divide by zero."
MESSAGE_GOODBYE: str = "Goodbye!"

## ASCII title shown at start: a calculator with the lettering to its right.
ASCII_TITLE: str = r"""
 _____________________
|  _________________  |
| |               0 | |
| |_________________| |
|  ___ ___ ___   ___  |     ____        _            _       _
| | 7 | 8 | 9 | | + | |    / ___|__ _  | | ___ _   _| | __ _| |_ ___  _ __
| |___|___|___| |___| |   | |   / _` | | |/ __| | | | |/ _` | __/ _ \| '__|
| | 4 | 5 | 6 | | - | |   | |__| (_| | | | (__| |_| | | (_| | || (_) | |
| |___|___|___| |___| |    \____\__,_| |_|\___|\__,_|_|\__,_|\__\___/|_|
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""
