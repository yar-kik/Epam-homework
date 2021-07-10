"""
Create a function sum_binary_1 that for a positive integer n
calculates the result value, which is equal to the sum of the
“1” in the binary representation of n otherwise, returns None.

Example,
n = 14 = 1110 result = 3
n = 128 = 10000000 result = 1
"""


from typing import Optional


def sum_binary_1(n: int) -> Optional[int]:
    """
    calculates the result value, which is equal to the sum of the “1”
    in the binary representation of n.
    @param n: Input integer.
    @return: Sum of the '1' in binary representation.
    """
    if not isinstance(n, int) or n <= 0:
        return None
    binary_repr = str(bin(n))[2:]
    return sum(list(map(int, binary_repr)))
