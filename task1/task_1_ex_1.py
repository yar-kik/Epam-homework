"""01-Task1-Task1
Write a Python-script that performs simple arithmetic operations: '+', '-', '*', '/'. The type of operator and
data are set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py 1 * 2

Notes:
For other operations need to raise NotImplementedError.
Do not dynamically execute your code (for example, using exec()).
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""
import argparse
from operator import add, sub, truediv, mul
from typing import Union

MATH_OPERATIONS = {
    "+": add,
    "-": sub,
    "/": truediv,
    "*": mul,
}


def calculate(first_number: float,
              operation: str,
              second_number: float) -> float:
    """
        Function calculates arithmetic expression.
        If arithmetic operation not "+","-","*" or "/" raise NotImplementedError

        :param first_number: number to calculate
        :param second_number: other number to calculate
        :param operation: one of simple arithmetic operation ("+","-","*" or "/")
        :return: result of arithmetic expression
        """
    if operation in MATH_OPERATIONS:
        return MATH_OPERATIONS[operation](first_number, second_number)
    else:
        raise NotImplementedError


def main():
    parser = argparse.ArgumentParser(description="Simple console calculator")
    parser.add_argument("first_number", type=float)
    parser.add_argument("operation", type=str)
    parser.add_argument("second_number", type=float)
    args = parser.parse_args()

    print(calculate(args.first_number,
                    args.operation,
                    args.second_number))


if __name__ == '__main__':
    main()
