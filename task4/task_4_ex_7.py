"""
Task04_1_7
Implement a function foo(List[int]) -> List[int] which, given a list of integers, returns a new  or modified list
in which every element at index i of the new list is the product of all the numbers in the original array except the one at i.
Example:
`python

foo([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]

foo([3, 2, 1])
[2, 3, 6]`
"""
from functools import reduce
from typing import List


def product_array(num_list: List[int]) -> List[int]:
    """
    Function returns a new  or modified list in
    which every element at index i of the new list is the product of all the
    numbers in the original array except the one at i.
    @param num_list: list of integers
    @return: product list
    """
    number_product = []
    for i in range(len(num_list)):
        number_product.append(
            reduce(int.__mul__, num_list[:i] + num_list[i + 1:]))
    return number_product
