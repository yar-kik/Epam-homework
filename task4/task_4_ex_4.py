"""
Implement a function `split_by_index(string: str, indexes: List[int]) -> List[str]`
which splits the `string` by indexes specified in `indexes`. 
Only positive index, larger than previous in list is considered valid.
Invalid indexes must be ignored.

Examples:
```python
>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 8, -4, 0, "u", 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("no luck", [42])
["no luck"]
```
"""
from typing import List


def get_correct_indexes(max_index: int, indexes: List[int]) -> List[int]:
    """
    Return list with with positive indexes and every next
    larger than previous. Non-numerable and out-of-range values ignores.
    @param max_index: maximum possible index
    @param indexes: list of input indexes
    @return: correct output indexes
    """
    indexes = [i for i in indexes if
               isinstance(i, int) and 0 < i < max_index]
    if not indexes:
        return []
    new_indexes = [indexes[0]]
    for i in indexes[1:]:
        if new_indexes[-1] < i:
            new_indexes.append(i)
    return new_indexes


def split_by_index(string: str, indexes: List[int]) -> List[str]:
    """
    Function to slit string by list of indexes
    @param string: string to slit
    @param indexes: list of indexes to split by
    @return: split string
    """
    indexes = get_correct_indexes(len(string), indexes)
    if not indexes:
        return [string]
    split_string = []
    chunk = ''
    k = 0
    for i, character in enumerate(string):
        if k < len(indexes) and i == indexes[k]:
            split_string.append(chunk)
            chunk = character
            k += 1
        else:
            chunk += character
    split_string.append(chunk)
    return split_string

