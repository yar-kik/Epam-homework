"""Task 1
For a given integer n calculate the value which is equal to a:
- squared number, if its value is strictly positive;
- modulus of a number, if its value is strictly negative;
- zero, if the integer n is zero.

Example,
n = 4 result = 16
n = -5 result = 5
n = 0 result = 0

Example of how the task should be called:
python3 task_3_ex_1.py 4

Note: use argparse module for parsing arguments from CLI
"""
from argparse import ArgumentParser


def calculate(n: int) -> int:
    """
    Calculate expression.
    @param n: integer to calculate.
    @return: calculation result.
    """
    if n >= 0:
        return n ** 2
    return abs(n)


def main() -> None:
    """
    Main function
    @return: None
    """
    parser = ArgumentParser()
    parser.add_argument('n', type=int, help="Integer to calculate")
    args = parser.parse_args()
    result = calculate(args.n)
    print(result)


if __name__ == '__main__':
    main()
