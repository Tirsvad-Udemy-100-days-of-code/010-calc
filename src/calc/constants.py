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

## ASCII title shown when the program starts.
ASCII_TITLE: str = r"""
  ____        _            _       _
 / ___|__ _  | | ___ _   _| | __ _| |_ ___  _ __
| |   / _` | | |/ __| | | | |/ _` | __/ _ \| '__|
| |__| (_| | | | (__| |_| | | (_| | || (_) | |
 \____\__,_| |_|\___|\__,_|_|\__,_|\__\___/|_|
"""

## ASCII calculator shown under the title.
ASCII_CALCULATOR: str = r"""
 _____________________
|  _________________  |
| |               0 | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""
