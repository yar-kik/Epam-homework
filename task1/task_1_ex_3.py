""" Write a Python-script that determines whether the input string is the correct entry for the
'formula' according EBNF syntax (without using regular expressions).
Formula = Number | (Formula Sign Formula)
Sign = '+' | '-'
Number = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
Input: string
Result: (True / False, The result value / None)

Example,
user_input = '1+2+4-2+5-1' result = (True, 9)
user_input = '123' result = (True, 123)
user_input = 'hello+12' result = (False, None)
user_input = '2++12--3' result = (False, None)
user_input = '' result = (False, None)

Example how to call the script from CLI:
python task_1_ex_3.py 1+5-2

Hint: use argparse module for parsing arguments from CLI
"""
from argparse import ArgumentParser
from typing import Optional, Tuple


ALLOWED_CHARS = ['0', '1', '2', '3', '4', '5',
                 '6', '7', '8', '9', '+', '-']


def check_formula(expression: str) -> Tuple[bool, Optional[int]]:
    """
    Check input string and if it's correct - calculate this expression.
    :param expression: math expression which includes numbers and sign "+"|"-".
    :return: True|result of math expression if success and False|None
    otherwise.
    """
    contains_invalid_character = any(
        [element for element in expression if element not in ALLOWED_CHARS])
    if not expression \
            or "++" in expression \
            or "--" in expression \
            or contains_invalid_character:
        return False, None
    if expression.isdigit():
        return True, int(expression)
    result = 0
    try:
        for element in expression.split('+'):
            if '-' in element:
                subelements = list(map(int, element.split('-')))
                element = subelements[0] - sum(subelements[1:])
            result += int(element)
        return True, result
    except ValueError:
        return False, None


def main():
    parser = ArgumentParser(
        description="Console calculator that performs "
                    "standard math operations on the data")
    parser.add_argument("user_input", type=str)
    args = parser.parse_args()

    print(check_formula(args.user_input))


if __name__ == '__main__':
    main()

