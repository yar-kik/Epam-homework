"""
Task 04-Task 1.8
Implement a function which takes a list of elements and returns a list of tuples containing pairs of this elements.
Pairs should be formed as in the example. If there is only one element in the list return `None`
instead.
Using zip() is prohibited.

Examples:
>>> get_pairs([1, 2, 3, 8, 9])
[(1, 2), (2, 3), (3, 8), (8, 9)]

>>> get_pairs(['need', 'to', 'sleep', 'more'])
[('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]

>>> get_pairs([1])
None
"""
from typing import Optional, Union, List


def get_pairs(lst: List[Union[str, int]]) -> Optional[list]:
    """
    function which takes a list of elements and returns a list of tuples
    containing pairs of this elements.
    @param lst: list with elements.
    @return: list of tuples containing pairs of this elements.
    """
    if 2 > len(lst) >= 0:
        return None
    pairs_list = list(map(lambda x, y: (x, y), lst[:-1], lst[1:]))
    return pairs_list
