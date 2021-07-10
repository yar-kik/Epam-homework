"""
For a positive integer n calculate the result value, which is equal to the sum
of the odd numbers of n.

Example,
n = 1234 result = 4
n = 246 result = 0

Write it as function.

Note:
Raise TypeError in case of wrong data type or negative integer;
Use of 'functools' module is prohibited, you just need simple for loop.
"""


def sum_odd_numbers(n: int) -> int:
    """
    Sum the odd numbers of n
    @param n: input number
    @return: result of sum
    """
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise TypeError
    integers = list(map(int, str(n)))
    result = sum([i for i in integers if i % 2])
    return result

