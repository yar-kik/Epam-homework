"""01-Task1-Task2
Write a Python-script that performs the standard math functions on the data. The name of function and data are
set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py add 1 2

Notes:
Function names must match the standard mathematical, logical and comparison functions from the built-in libraries.
The script must raises all happened exceptions.
For non-mathematical function need to raise NotImplementedError.
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""
import argparse
import math
import operator
from typing import Union


def calculate(operation: str, integers: list) -> Union[int, float]:
    """
    Function to calculate math expression.
    :param operation: standard math function from built-in libraries
    :param integers: list with two integer to calculate
    :return: result of a calculation
    """

    if operation in dir(math):
        return getattr(math, operation)(*integers)
    elif operation in dir(operator):
        return getattr(operator, operation)(*integers)
    raise NotImplementedError


def main() -> None:
    """
    Main function to calculate and return result in console
    :return: None
    """
    parser = argparse.ArgumentParser(
        description="Console calculator that performs "
                    "standard math operations on the data",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "operation", type=str,
        help="Math operation for calculation. Use built-in functions"
    )
    parser.add_argument(
        "integers", type=float, nargs="*", metavar="N",
        help="Integers to calculate"
    )
    args = parser.parse_args()

    print(calculate(args.operation,
                    args.integers))


if __name__ == '__main__':
    main()
