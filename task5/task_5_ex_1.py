"""
Write 2 functions:
1. Function 'is_sorted', determining whether a given list of integer values of arbitrary length
is sorted in a given order (the order is set up by enum value SortOrder).
List and sort order are passed by parameters. Function does not change the array, it returns
boolean value.

2. Function 'transform', replacing the value of each element of an integer list with the sum
of this element value and its index, only if the given list is sorted in the given order
(the order is set up by enum value SortOrder). List and sort order are passed by parameters.
To check, if the array is sorted, the function 'is_sorted' is called.

Example for 'transform' function,
For [5, 17, 24, 88, 33, 2] and “ascending” sort order values in the array do not change;
For [15, 10, 3] and “ascending” sort order values in the array do not change;
For [15, 10, 3] and “descending” sort order the values in the array are changing to [15, 11, 5]

Note:
Raise TypeError in case of wrong function arguments data type;
"""
from enum import Enum
from typing import List


class SortOrder(Enum):
    """
    Enumeration for sorting order.
    """
    ASC = "ASCENDING"
    DESC = "DESCENDING"


def is_sorted(num_list: List[int], sort_order: SortOrder) -> bool:
    """
    Determining whether a given list of integer values of arbitrary length
    is sorted in a given order.
    @param num_list: list of numbers to check.
    @param sort_order: sort order (descending or ascending).
    @return: result of type bool.
    """
    contain_invalid_data = any([i for i in num_list
                                if not isinstance(i, int)])
    if contain_invalid_data \
            or not num_list \
            or not isinstance(sort_order, SortOrder):
        raise TypeError
    for x, y in zip(num_list[:-1], num_list[1:]):
        if sort_order is SortOrder.ASC and x > y \
                or sort_order is SortOrder.DESC and x < y:
            return False
    return True


def transform(num_list: List[int], sort_order: SortOrder) -> List[int]:
    """
    Function replaces the value of each element of an integer list with the
    sum of this element value and its index, only if the given list is sorted
    in the given order.
    @param num_list: list of number.
    @param sort_order: sorting order (descending or ascending).
    @return: changed array if list of number is sorted.
    """
    if is_sorted(num_list, sort_order):
        num_list = [i + num for i, num in enumerate(num_list)]
    return num_list
