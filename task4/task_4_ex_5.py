"""Implement a function `get_digits(args: int) -> Tuple[int]` which receives 
arbitrary amount of arguments and returns a tuple of digits of given integers.

Example:
```python
>>> split_by_index(8717, 82911, 99)
(8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
```
"""
from functools import reduce
from typing import Tuple


def get_digits(*args: int) -> Tuple[int]:
    """
    Function which receives arbitrary amount of arguments and return a tuple
    of given integers
    @param args:
    @return:
    """
    # concatenate all numbers in one string
    str_numbers = reduce(str.__add__, map(str, args))
    digits = tuple([int(digit) for digit in str_numbers])
    return digits

